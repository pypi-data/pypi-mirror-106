(self["webpackChunkorbitcontrol_patch"] = self["webpackChunkorbitcontrol_patch"] || []).push([["lib_index_js"],{

/***/ "./lib/OrbitControls.js":
/*!******************************!*\
  !*** ./lib/OrbitControls.js ***!
  \******************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "OrbitControlsModel": () => (/* binding */ OrbitControlsModel),
/* harmony export */   "OrbitControlsView": () => (/* binding */ OrbitControlsView)
/* harmony export */ });
/* harmony import */ var jupyter_threejs__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! jupyter-threejs */ "webpack/sharing/consume/default/jupyter-threejs/jupyter-threejs");
/* harmony import */ var jupyter_threejs__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(jupyter_threejs__WEBPACK_IMPORTED_MODULE_0__);


var OrbitControlsModel = jupyter_threejs__WEBPACK_IMPORTED_MODULE_0__.OrbitControlsModel.extend({

    setupListeners: function () {
        jupyter_threejs__WEBPACK_IMPORTED_MODULE_0__.OrbitControlsModel.prototype.setupListeners.call(this);
        console.log("OrbitControls update");
        this.obj.update()
    }
});

const OrbitControlsView = jupyter_threejs__WEBPACK_IMPORTED_MODULE_0__.OrbitControlsView;


/***/ }),

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

// Export widget models and views, and the npm package version number.
module.exports = __webpack_require__(/*! ./OrbitControls.js */ "./lib/OrbitControls.js");
module.exports.version = __webpack_require__(/*! ../package.json */ "./package.json").version;


/***/ }),

/***/ "./package.json":
/*!**********************!*\
  !*** ./package.json ***!
  \**********************/
/***/ ((module) => {

"use strict";
module.exports = JSON.parse('{"name":"orbitcontrol_patch","version":"0.1.0","description":"A patch for pythreejs Orbitcontrol to update at init","author":"Bernhard Walter","main":"lib/index.js","repository":{"type":"git","url":"https://github.com/bernhard-42/orbitcontrol-patch.git"},"keywords":["jupyter","widgets","ipython","ipywidgets","jupyterlab-extension"],"files":["lib/**/*.js","dist/*.js"],"scripts":{"clean":"rimraf dist/ && rimraf ../orbitcontrol_patch/labextension/ && rimraf ../orbitcontrol_patch/nbextension","prepublish":"yarn run clean && yarn run build:prod","build":"webpack --mode=development && yarn run build:labextension:dev","build:prod":"webpack --mode=production && yarn run build:labextension","build:labextension":"jupyter labextension build .","build:labextension:dev":"jupyter labextension build --development True .","watch":"webpack --watch --mode=development","test":"echo \\"Error: no test specified\\" && exit 1"},"devDependencies":{"@jupyterlab/builder":"^3.0.0","webpack":"^5","rimraf":"^2.6.1","yarn":"^1.22.0"},"dependencies":{"@jupyter-widgets/base":"^1.1 || ^2 || ^3 || ^4","jupyter-threejs":"^2.3.0"},"jupyterlab":{"extension":"lib/labplugin","outputDir":"../orbitcontrol_patch/labextension","sharedPackages":{"@jupyter-widgets/base":{"bundled":false,"singleton":true}}}}');

/***/ })

}]);
//# sourceMappingURL=lib_index_js.68ebafdb93792e2242c3.js.map