(self["webpackChunkjupyterlab_notebookbuttons"] = self["webpackChunkjupyterlab_notebookbuttons"] || []).push([["lib_index_js"],{

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "ButtonExtension": () => (/* binding */ ButtonExtension),
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _lumino_disposable__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/disposable */ "webpack/sharing/consume/default/@lumino/disposable");
/* harmony import */ var _lumino_disposable__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_disposable__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/notebook */ "webpack/sharing/consume/default/@jupyterlab/notebook");
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @lumino/algorithm */ "webpack/sharing/consume/default/@lumino/algorithm");
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_lumino_algorithm__WEBPACK_IMPORTED_MODULE_4__);





/**
 * A notebook widget extension that adds a button to the toolbar.
 */
class ButtonExtension {
    constructor(setting_registry) {
        this.setting_registry = setting_registry;
        console.log('constructor');
        // read the settings
        this.setup_settings();
    }
    setup_settings() {
        Promise.all([this.setting_registry.load(extension.id)])
            .then(([settings]) => {
            console.log('reading settings');
            this.settings = settings;
            // update of settings is done automatically
            //settings.changed.connect(() => {
            //  this.update_settings(settings);
            //});
        })
            .catch((reason) => {
            console.error(reason.message);
        });
    }
    /**
     * Create a new extension object.
     */
    createNew(panel, context) {
        // read all settings
        const have_runall = this.settings.get('runall').composite;
        const have_clearalloutputs = this.settings.get('clearalloutputs').composite;
        const have_deletecells = this.settings.get('deletecells').composite;
        let insert_before = this.settings.get('insertbefore').composite.toString();
        // sanity check, if insert_before doesn't exist use the first element ...
        const names = (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_4__.toArray)(panel.toolbar.names());
        if (names.includes(insert_before) === false) {
            insert_before = names[0];
        }
        const callback_clearall = () => {
            _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_2__.NotebookActions.clearAllOutputs(panel.content);
        };
        const callback_deletecells = () => {
            _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_2__.NotebookActions.deleteCells(panel.content);
        };
        const callback_runall = () => {
            _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_2__.NotebookActions.runAll(panel.content, context.sessionContext);
        };
        const clearall_button = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ToolbarButton({
            className: 'jp-nb-buttons',
            iconClass: 'fa fa-snowplow',
            onClick: callback_clearall,
            tooltip: 'Clear All Outputs'
        });
        const deletecells_button = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ToolbarButton({
            className: 'jp-nb-buttons',
            iconClass: 'fa fa-trash-alt',
            onClick: callback_deletecells,
            tooltip: 'Delete Cells'
        });
        const runall_button = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ToolbarButton({
            className: 'jp-nb-buttons',
            iconClass: 'fa fa-fast-forward',
            onClick: callback_runall,
            tooltip: 'Run all'
        });
        // start column to append the icons
        if (have_deletecells === true) {
            panel.toolbar.insertBefore(insert_before, 'jp-nb-deletecells', deletecells_button);
        }
        if (have_runall === true) {
            panel.toolbar.insertBefore(insert_before, 'jp-nb-runall', runall_button);
        }
        if (have_clearalloutputs === true) {
            panel.toolbar.insertBefore(insert_before, 'jp-nb-cleaarall', clearall_button);
        }
        return new _lumino_disposable__WEBPACK_IMPORTED_MODULE_0__.DisposableDelegate(() => {
            if (have_deletecells === true) {
                deletecells_button.dispose();
            }
            if (have_runall === true) {
                runall_button.dispose();
            }
            if (have_clearalloutputs === true) {
                clearall_button.dispose();
            }
        });
    }
}
/**
 * Activate the extension.
 */
function activate(app, setting_registry) {
    app.docRegistry.addWidgetExtension('Notebook', new ButtonExtension(setting_registry));
    console.debug('JupyterLab extension jupyterlab_notebookbuttons is activated!');
}
/**
 * Initialization data for the jupyterlab_nbgrader extension.
 */
const extension = {
    id: 'jupyterlab_notebookbuttons:plugin',
    autoStart: true,
    requires: [_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_3__.ISettingRegistry],
    activate: activate
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (extension);


/***/ })

}]);
//# sourceMappingURL=lib_index_js.0f01e274506f54ecc1fd.js.map