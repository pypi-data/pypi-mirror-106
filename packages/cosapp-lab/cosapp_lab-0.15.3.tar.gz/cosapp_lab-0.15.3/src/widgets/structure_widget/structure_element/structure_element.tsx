import React, { Component, forwardRef } from 'react';
import { withStyles } from '@material-ui/core';
import { Styles } from '@material-ui/styles/withStyles';
import { Theme } from '@material-ui/core/styles';
import { connect } from 'react-redux';
import { StateInterface, IDict } from '../../redux/types';
import { debounce } from '../../redux/tools';
import * as ReduxAction from '../../redux/actions';
import Button from '@material-ui/core/Button';
import { DataSet, Network, DataView } from 'vis';
import FormControl from '@material-ui/core/FormControl';
import MenuItem from '@material-ui/core/MenuItem';
import Select from '@material-ui/core/Select';
import { create_UUID } from '../../../utils/tools';
import 'vis/dist/vis.min.css';

const styles: Styles<Theme, any> = (theme: Theme) => ({
  textColor: {
    color: 'rgb(250, 250, 250)',
    background: '#525354',
    margin: '0px 5px',
  },
});

const getGraphData = (state: StateInterface) => {
  return {};
};

const mapStateToProps = (state: StateInterface) => {
  return getGraphData(state);
};

const mapDispatchToProps = (dispatch: (f: any) => void) => {
  return {};
};

interface IState {
  traceConfig: IDict<any>;
  network: any;
  rawData: { nodes: any[]; edges: any[] };
  nodes: DataSet;
  edges: DataSet;
  systems: string[];
  options: IDict<any>;
  divID: string;
}

interface IProps {
  send_msg: any;
  model: any;
  classes: any;
  initialState: IDict<any>;
}

export class StructureElement extends Component<IProps, IState> {
  private _divRef: React.RefObject<HTMLDivElement>;
  _network: any;
  private _resizeHandler: any;
  constructor(props: IProps) {
    super(props);
    props.model.listenTo(props.model, 'msg:custom', this.on_msg);
    this._network = null;
    let traceConfig: {
      bgColor: number;
    };
    if (props.initialState) {
      traceConfig = props.initialState.traceConfig;
      if (!traceConfig.bgColor) {
        traceConfig['bgColor'] = 0;
      }
    } else {
      traceConfig = { bgColor: 0 };
    }
    this.state = {
      divID: create_UUID(),
      network: null,
      traceConfig,
      rawData: { nodes: [], edges: [] },
      nodes: null,
      edges: null,
      systems: [],
      options: {
        layout: {
          hierarchical: false,
          randomSeed: 8,
        },
        nodes: {
          shape: 'circle',
        },
      },
    };
  }

  on_msg = (
    data: { type: string; payload: { [key: string]: any } },
    buffer: any[]
  ) => {
    const { type, payload } = data;

    switch (type) {
      case 'StructureView::structureData': {
        const rawData = JSON.parse(
          JSON.stringify({
            nodes: payload['nodes'],
            edges: payload['edges'],
          })
        );
        const { groups, title } = payload;
        const nodes = new DataSet(payload['nodes']);
        const edges = new DataSet(payload['edges']);
        const network_data = {
          nodes,
          edges,
        };
        this._network = this.generateNetwork(
          network_data,
          this.state.options,
          false
        );
        // this._network = new Network(
        //   this._divRef.current,
        //   network_data,
        //   this.state.options
        // );
        this.setState((old) => ({
          ...old,
          nodes,
          edges,
          systems: groups,
          rawData,
        }));
        break;
      }
      case 'StructureView::importError': {
        this._divRef.current.innerHTML =
          'Structure widget requires CoSApp >= 0.11.5';
        break;
      }
    }
  };
  componentDidUpdate(prevProps: IProps, prevState: IState) {}

  componentDidMount() {
    this.props.send_msg({ action: 'StructureView::getData' });
    this._resizeHandler = debounce(this.measure, 500);
    window.addEventListener('resize', this._resizeHandler);
  }

  componentWillUnmount() {
    this.props.model.stopListening(this.props.model, 'msg:custom', this.on_msg);
    window.removeEventListener('resize', this._resizeHandler);
  }

  measure = (data) => {
    try {
      this._network.fit({ animation: true });
    } catch {}
  };

  bestFit = () => {
    const network = this._network;
    const nodes = this.state.nodes;
    if (!nodes || !network) {
      return;
    }
    network.moveTo({ scale: 1 });
    network.stopSimulation();
    const bigBB = {
      top: Infinity,
      left: Infinity,
      right: -Infinity,
      bottom: -Infinity,
    };
    nodes.getIds().forEach((i) => {
      const bb = network.getBoundingBox(i);
      if (bb.top < bigBB.top) {
        bigBB.top = bb.top;
      }
      if (bb.left < bigBB.left) {
        bigBB.left = bb.left;
      }
      if (bb.right > bigBB.right) {
        bigBB.right = bb.right;
      }
      if (bb.bottom > bigBB.bottom) {
        bigBB.bottom = bb.bottom;
      }
    });

    const canvasWidth = network.canvas.body.container.clientWidth;
    const canvasHeight = network.canvas.body.container.clientHeight;

    const scaleX = canvasWidth / (bigBB.right - bigBB.left);
    const scaleY = canvasHeight / (bigBB.bottom - bigBB.top);
    let scale = scaleX;
    if (scale * (bigBB.bottom - bigBB.top) > canvasHeight) {
      scale = scaleY;
    }

    if (scale > 1) {
      scale = 0.9 * scale;
    }

    network.moveTo({
      scale: scale,
      position: {
        x: (bigBB.right + bigBB.left) / 2,
        y: (bigBB.bottom + bigBB.top) / 2,
      },
    });
  };

  generateNetwork = (data_, options_, hierarchicalLayout) => {
    if (this._network) {
      this._network.destroy();
    }

    const container = document.getElementById(this.state.divID);
    const network_ = new Network(container, data_, options_);

    if (!hierarchicalLayout) {
      // Cluster from double-clicked node
      network_.on('doubleClick', (params) => {
        if (params.nodes.length === 1) {
          if (network_.isCluster(params.nodes[0]) === false) {
            this.clusterFromSelection(params.nodes[0]);
          }
        }
      });

      // Suppress cluster when click on
      network_.on('selectNode', (params) => {
        if (params.nodes.length === 1) {
          if (network_.isCluster(params.nodes[0]) === true) {
            network_.openCluster(params.nodes[0]);
          }
        }
      });

      // Force fit once the system is stabilized
      network_.on('stabilized', (params) => {
        network_.fit({ animation: true });
      });
    }

    return network_;
  };

  clusterSystem = (system, system_name, group_name, nodes) => {
    const clusterOptionsByData = {
      joinCondition: function(childOptions) {
        return childOptions.group === system; // the system is fully defined in the node.
      },
      processProperties: function(clusterOptions, childNodes, childEdges) {
        const hidden_node = nodes.get({
          filter: function(node) {
            return node.label === system_name;
          },
        });
        clusterOptions.title = hidden_node[0].title;
        return clusterOptions;
      },
      clusterNodeProperties: {
        id: 'cluster:' + system,
        borderWidth: 3,
        shape: 'database',
        label: system_name,
        group: group_name,
        allowSingleNodeCluster: true,
      },
    };
    this._network.cluster(clusterOptionsByData);
  };

  clusterBySystem = () => {
    const network_data = {
      nodes: this.state.nodes,
      edges: this.state.edges,
    };
    const options = this.state.options;
    this._network = this.generateNetwork(network_data, options, false);
    for (let i = 0; i < this.state.systems.length; i++) {
      const system = this.state.systems[i];
      const hierarchy = system.split('.');
      const system_name = hierarchy.pop();

      if (hierarchy.length === 0) continue; // Don't group last level

      this.clusterSystem(
        system,
        system_name,
        hierarchy.join('.'),
        this.state.nodes
      );
    }
  };

  setHierarchicalLayout = () => {
    const hierarchyView = new DataView(this.state.nodes, {
      filter: (item) => {
        return item.label !== undefined && item.label.length > 0;
      },
      fields: ['id', 'label', 'title', 'group', 'shape', 'level'],
    });

    const hierarchyEdges = [];
    this.state.rawData.edges.forEach((item) => {
      if (item.hidden !== undefined && item.hidden) {
        let newItem = JSON.parse(JSON.stringify(item));
        delete newItem['hidden'];
        hierarchyEdges.push(newItem);
      }
    });

    const data_ = {
      nodes: hierarchyView,
      edges: new DataSet(hierarchyEdges),
    };

    const options_ = {
      layout: {
        hierarchical: {
          enabled: true,
        },
      },
      physics: false,
    };
    this._network = this.generateNetwork(data_, options_, true);
  };

  clusterFromSelection = (node_idx) => {
    const selected_node = this.state.nodes.get(node_idx);
    const systems = this.state.systems;
    // Extract list of groups at selected_node level or below
    const subsystems = [];
    for (let i = systems.length - 1; i >= 0; i--) {
      // Cluster all nodes at selected_node or below + keep all existing cluster
      if (
        systems[i].startsWith(selected_node.group) ||
        this._network.isCluster('cluster:' + systems[i])
      ) {
        subsystems.unshift(systems[i]);
      }
    }

    const network_data = {
      nodes: this.state.nodes,
      edges: this.state.edges,
    };
    this._network.setData(network_data);

    for (let i = 0; i < subsystems.length; i++) {
      let system = subsystems[i];
      let hierarchy = system.split('.');
      let system_name = hierarchy.pop();

      this.clusterSystem(
        system,
        system_name,
        hierarchy.join('.'),
        this.state.nodes
      );
    }
  };

  resetAllClusters = () => {
    const network_data = {
      nodes: this.state.nodes,
      edges: this.state.edges,
    };
    this._network = this.generateNetwork(
      network_data,
      this.state.options,
      false
    );
  };
  render() {
    return (
      <div className={'cosapp-widget-box'}>
        <div
          className={this.state.traceConfig['bgColor'] === 1 ? 'pbsView' : null}
          id={this.state.divID}
          style={{ height: 'calc(100% - 30px)' }}></div>
        <div style={{ height: '30px', display: 'flex', background: '#e0e0e0' }}>
          <Button onClick={this.clusterBySystem}>Cluster view</Button>
          <Button onClick={this.setHierarchicalLayout}>
            Hierarchical view
          </Button>
          <Button
            onClick={() => {
              this.props.send_msg({ action: 'StructureView::getData' });
            }}>
            Refresh
          </Button>

          <FormControl style={{ marginRight: 10, marginLeft: 10 }}>
            <Select
              value={this.state.traceConfig['bgColor']}
              onChange={(event: React.ChangeEvent<{ value: unknown }>) => {
                this.setState((old) => ({
                  ...old,
                  traceConfig: {
                    ...old.traceConfig,
                    bgColor: event.target.value as number,
                  },
                }));
              }}>
              <MenuItem value={1}>Dark</MenuItem>
              <MenuItem value={0}>Light</MenuItem>
            </Select>
          </FormControl>
        </div>
      </div>
    );
  }
}

export default connect(mapStateToProps, mapDispatchToProps, null, {
  forwardRef: true,
})(
  withStyles(styles)(
    forwardRef((props: IProps, ref: any) => (
      <StructureElement {...props} ref={ref} />
    ))
  )
);
