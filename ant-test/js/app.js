//var Menu = antd.Menu;
//var SubMenu = Menu.SubMenu;

var Header = React.createClass({
  render() {
    return (
      <div>1222</div>
      <a class="logo" href="http://www.baidu.com">
        <img width="60px" src="https://t.alipayobjects.com/images/rmsweb/>
        EasyHexo
      </a>
    );
  }
});

React.render(<Header />, document.getElementById('header'));

/*
var Sider = React.createClass({
  getInitialState() {
    return {
      current: '1'
    }
  },
  handleClick(e) {
    console.log('click ', e);
    this.setState({
      current: e.key
    });
  },
  render() {
    return <Menu onClick={this.handleClick}
                 style={{width:260}}
                 defaultOpenKeys={['sub1']}
                 selectedKeys={[this.state.current]}
                 mode="inline">
      <SubMenu key="sub1" title={<span><i className="anticon anticon-mail"></i><span>文章管理</span></span>}>
        <Menu.Item key="1">
          <a href="/new" >新建文章</a>
        </Menu.Item>
        <Menu.Item key="2">文章列表</Menu.Item>
      </SubMenu>
      <SubMenu key="sub2" title={<span><i className="anticon anticon-appstore"></i><span>博客设置</span></span>}>
        <Menu.Item key="5">Hexo设置</Menu.Item>
        <Menu.Item key="6">主题设置</Menu.Item>
      </SubMenu>
      <SubMenu key="sub3" title={<span><i className="anticon anticon-setting"></i><span>关于</span></span>}>
        <Menu.Item key="9">选项9</Menu.Item>
        <Menu.Item key="10">选项10</Menu.Item>
        <Menu.Item key="11">选项11</Menu.Item>
        <Menu.Item key="12">选项12</Menu.Item>
      </SubMenu>
    </Menu>;
  }
});

React.render(<Sider />, document.getElementById('sider'));
*/
