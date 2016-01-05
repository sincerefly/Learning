var CheckLink = React.createClass({
  render: function() {
    // 这样会把 CheckList 所有的 props 复制到 <a>
    return <a {...this.props}>{'√ '}{this.props.children}</a>;
  }
});

var LikeButton = React.createClass({
  getInitialState: function () {
    return {liked: false};
  },
  handleClick: function () {
    this.setState({liked: !this.state.liked}, function () {
      console.log("console-31031");
    });
  },
  render: function () {
    var text = this.state.liked ? 'like': 'haven\'t like';
    return (
      <p onClick={this.handleClick}>
        You {text} this. Click to toggle
      </p>
    );
  }
});

var HomePage = React.createClass({
  render: function () {
    return (
      <div>
        <div>The time is: {this.props.date.toTimeString()}</div>
        <LikeButton />
        <CheckLink href="/checked.html">
          Click here!
        </CheckLink>
      </div>
    );
  }
});


setInterval(function () {
  React.render(
    <HomePage date={new Date()}/>,
    document.getElementById("content"));
}, 500);
