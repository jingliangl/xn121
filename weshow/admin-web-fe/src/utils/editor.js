import Handsontable from 'handsontable/dist/handsontable.full.js'

module.exports.kwEditor = Handsontable.editors.DateEditor.prototype.extend();

module.exports.kwRenderer = function (instance, td, row, col, prop, value, cellProperties) {
    var escaped = Handsontable.helper.stringify(value);
    var img;

    if (escaped.indexOf('http') === 0) {
        img = document.createElement('IMG');
        img.src = value;

        Handsontable.Dom.addEvent(img, 'mousedown', function (e) {
            e.preventDefault(); // prevent selection quirk
        });

        Handsontable.Dom.empty(td);
        td.appendChild(img);
    } else {
        Handsontable.renderers.TextRenderer.apply(this, arguments);
    }

    return td;
};
