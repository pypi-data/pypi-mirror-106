!function(e){var n={};function t(i){if(n[i])return n[i].exports;var r=n[i]={i:i,l:!1,exports:{}};return e[i].call(r.exports,r,r.exports,t),r.l=!0,r.exports}t.m=e,t.c=n,t.d=function(e,n,i){t.o(e,n)||Object.defineProperty(e,n,{enumerable:!0,get:i})},t.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},t.t=function(e,n){if(1&n&&(e=t(e)),8&n)return e;if(4&n&&"object"==typeof e&&e&&e.__esModule)return e;var i=Object.create(null);if(t.r(i),Object.defineProperty(i,"default",{enumerable:!0,value:e}),2&n&&"string"!=typeof e)for(var r in e)t.d(i,r,function(n){return e[n]}.bind(null,r));return i},t.n=function(e){var n=e&&e.__esModule?function(){return e.default}:function(){return e};return t.d(n,"a",n),n},t.o=function(e,n){return Object.prototype.hasOwnProperty.call(e,n)},t.p="",t(t.s=155)}({155:function(e,n){function t(e,n){for(var t=0;t<n.length;t++){var i=n[t];i.enumerable=i.enumerable||!1,i.configurable=!0,"value"in i&&(i.writable=!0),Object.defineProperty(e,i.key,i)}}(function(e){var n=[],i="/static/js/vendor/tinymce/js/tinymce/skins/studio-tmce4/skin.min.css",r=void 0!==window.LmsRuntime,o="/static/studio/js/vendor/tinymce/js/tinymce/skins/studio-tmce4/content.min.css";r&&(o="/static/js/vendor/tinymce/js/tinymce/skins/studio-tmce4/content.min.css"),void 0===window.tinymce&&(n.push("tinymce"),n.push("jquery.tinymce"),$("link[href='".concat(i,"']")).length||$('<link href="'.concat(i,'" type="text/css" rel="stylesheet" />')).appendTo("head")),e(n,(function(){var e=function(){function e(){var n,t,i;!function(e,n){if(!(e instanceof n))throw new TypeError("Cannot call a class as a function")}(this,e),i=[],(t="editorInstances")in(n=this)?Object.defineProperty(n,t,{value:i,enumerable:!0,configurable:!0,writable:!0}):n[t]=i}var n,i,r;return n=e,(i=[{key:"getTinyMCEConfig",value:function(e){var n=this,t={menubar:!1,statusbar:!1,theme:"modern",skin:"studio-tmce4",height:"300",schema:"html5",plugins:"code image link lists",content_css:o,toolbar:"formatselect | bold italic underline | link blockquote image | numlist bullist outdent indent | strikethrough | code | undo redo",setup:function(e){e.on("init",(function(){n.editorInstances.push(e)}))}};return e&&(t=Object.assign(t,{toolbar:!1,readonly:1})),t}},{key:"load",value:function(e){this.elements=e;var n=this;this.elements.each((function(){var e=$(this).attr("disabled"),t=$(this).attr("id");if(void 0!==t){var i=tinymce.get(t);i&&i.destroy()}var r=n.getTinyMCEConfig(e);$(this).tinymce(r)}))}},{key:"setOnChangeListener",value:function(e){var n=this;["change","keyup","drop","paste"].forEach((function(t){n.editorInstances.forEach((function(n){n.on(t,e)}))}))}},{key:"response",value:function(e){if(void 0===e)return this.editorInstances.map((function(e){return e.getContent().replace(/(\r\n|\n|\r)/gm,"")}));this.editorInstances.forEach((function(n,t){n.setContent(e[t])}))}}])&&t(n.prototype,i),r&&t(n,r),e}();return function(){return new e}}))}).call(window,window.define||window.RequireJS.define)}});
//# sourceMappingURL=openassessment-editor-tinymce.js.map