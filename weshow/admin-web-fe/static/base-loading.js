//重置所用客户端页面字体大小
window.onload = window.onresize = function() {
	var view_width = document.getElementsByTagName('html')[0].getBoundingClientRect().width;
	var _html = document.getElementsByTagName('html')[0];
	view_width > 640 ? _html.style.fontSize = 100 * (640 / 640) + 'px' : _html.style.fontSize = 100 * (view_width / 640) + 'px';
}
var view_width = document.getElementsByTagName("html")[0].getBoundingClientRect().width,
	_html = document.getElementsByTagName("html")[0];
_html.style.fontSize = view_width > 640 ? "100px" : 100 * (view_width / 640) + "px";
