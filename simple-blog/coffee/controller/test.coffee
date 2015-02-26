exports.hello = (req, res) ->
  #return res.jsonp {'hello':'world'}
  return res.send 'hello world'
