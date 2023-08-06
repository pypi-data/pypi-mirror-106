(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[6839],{66839:(e,t,s)=>{"use strict";s.r(t);s(53918);var r=s(55317),i=(s(32296),s(30879),s(99722)),o=s(44583),n=s(47181),a=(s(90806),s(52039),s(22814)),l=s(41682),c=s(77097),d=s(26765),h=s(11654);function p(){p=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(s){t.forEach((function(t){t.kind===s&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var s=e.prototype;["method","field"].forEach((function(r){t.forEach((function(t){var i=t.placement;if(t.kind===r&&("static"===i||"prototype"===i)){var o="static"===i?e:s;this.defineClassElement(o,t)}}),this)}),this)},defineClassElement:function(e,t){var s=t.descriptor;if("field"===t.kind){var r=t.initializer;s={enumerable:s.enumerable,writable:s.writable,configurable:s.configurable,value:void 0===r?void 0:r.call(e)}}Object.defineProperty(e,t.key,s)},decorateClass:function(e,t){var s=[],r=[],i={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,i)}),this),e.forEach((function(e){if(!f(e))return s.push(e);var t=this.decorateElement(e,i);s.push(t.element),s.push.apply(s,t.extras),r.push.apply(r,t.finishers)}),this),!t)return{elements:s,finishers:r};var o=this.decorateConstructor(s,t);return r.push.apply(r,o.finishers),o.finishers=r,o},addElementPlacement:function(e,t,s){var r=t[e.placement];if(!s&&-1!==r.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");r.push(e.key)},decorateElement:function(e,t){for(var s=[],r=[],i=e.decorators,o=i.length-1;o>=0;o--){var n=t[e.placement];n.splice(n.indexOf(e.key),1);var a=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,i[o])(a)||a);e=l.element,this.addElementPlacement(e,t),l.finisher&&r.push(l.finisher);var c=l.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);s.push.apply(s,c)}}return{element:e,finishers:r,extras:s}},decorateConstructor:function(e,t){for(var s=[],r=t.length-1;r>=0;r--){var i=this.fromClassDescriptor(e),o=this.toClassDescriptor((0,t[r])(i)||i);if(void 0!==o.finisher&&s.push(o.finisher),void 0!==o.elements){e=o.elements;for(var n=0;n<e.length-1;n++)for(var a=n+1;a<e.length;a++)if(e[n].key===e[a].key&&e[n].placement===e[a].placement)throw new TypeError("Duplicated element ("+e[n].key+")")}}return{elements:e,finishers:s}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return k(e,t);var s=Object.prototype.toString.call(e).slice(8,-1);return"Object"===s&&e.constructor&&(s=e.constructor.name),"Map"===s||"Set"===s?Array.from(e):"Arguments"===s||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(s)?k(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var s=y(e.key),r=String(e.placement);if("static"!==r&&"prototype"!==r&&"own"!==r)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+r+'"');var i=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var o={kind:t,key:s,placement:r,descriptor:Object.assign({},i)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(i,"get","The property descriptor of a field descriptor"),this.disallowProperty(i,"set","The property descriptor of a field descriptor"),this.disallowProperty(i,"value","The property descriptor of a field descriptor"),o.initializer=e.initializer),o},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:g(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var s=g(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:s}},runClassFinishers:function(e,t){for(var s=0;s<t.length;s++){var r=(0,t[s])(e);if(void 0!==r){if("function"!=typeof r)throw new TypeError("Finishers must return a constructor.");e=r}}return e},disallowProperty:function(e,t,s){if(void 0!==e[t])throw new TypeError(s+" can't have a ."+t+" property.")}};return e}function u(e){var t,s=y(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var r={kind:"field"===e.kind?"field":"method",key:s,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(r.decorators=e.decorators),"field"===e.kind&&(r.initializer=e.value),r}function m(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function f(e){return e.decorators&&e.decorators.length}function v(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function g(e,t){var s=e[t];if(void 0!==s&&"function"!=typeof s)throw new TypeError("Expected '"+t+"' to be a function");return s}function y(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var s=e[Symbol.toPrimitive];if(void 0!==s){var r=s.call(e,t||"default");if("object"!=typeof r)return r;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function k(e,t){(null==t||t>e.length)&&(t=e.length);for(var s=0,r=new Array(t);s<t;s++)r[s]=e[s];return r}!function(e,t,s,r){var i=p();if(r)for(var o=0;o<r.length;o++)i=r[o](i);var n=t((function(e){i.initializeInstanceElements(e,a.elements)}),s),a=i.decorateClass(function(e){for(var t=[],s=function(e){return"method"===e.kind&&e.key===o.key&&e.placement===o.placement},r=0;r<e.length;r++){var i,o=e[r];if("method"===o.kind&&(i=t.find(s)))if(v(o.descriptor)||v(i.descriptor)){if(f(o)||f(i))throw new ReferenceError("Duplicated methods ("+o.key+") can't be decorated.");i.descriptor=o.descriptor}else{if(f(o)){if(f(i))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+o.key+").");i.decorators=o.decorators}m(o,i)}else t.push(o)}return t}(n.d.map(u)),e);i.initializeClassElements(n.F,a.elements),i.runClassFinishers(n.F,a.finishers)}([(0,i.Mo)("dialog-hassio-snapshot")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,i.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,i.Cb)({attribute:!1})],key:"supervisor",value:void 0},{kind:"field",decorators:[(0,i.SB)()],key:"_error",value:void 0},{kind:"field",decorators:[(0,i.SB)()],key:"_onboarding",value:()=>!1},{kind:"field",decorators:[(0,i.SB)()],key:"_snapshot",value:void 0},{kind:"field",decorators:[(0,i.SB)()],key:"_folders",value:void 0},{kind:"field",decorators:[(0,i.SB)()],key:"_addons",value:void 0},{kind:"field",decorators:[(0,i.SB)()],key:"_dialogParams",value:void 0},{kind:"field",decorators:[(0,i.SB)()],key:"_snapshotPassword",value:void 0},{kind:"field",decorators:[(0,i.SB)()],key:"_restoreHass",value:()=>!0},{kind:"method",key:"showDialog",value:async function(e){var t,s,r,i;this._snapshot=await(0,c.Ju)(this.hass,e.slug),this._folders=(e=>{const t=[];return e.includes("homeassistant")&&t.push({slug:"homeassistant",name:"Home Assistant configuration",checked:!0}),e.includes("ssl")&&t.push({slug:"ssl",name:"SSL",checked:!0}),e.includes("share")&&t.push({slug:"share",name:"Share",checked:!0}),e.includes("addons/local")&&t.push({slug:"addons/local",name:"Local add-ons",checked:!0}),t})(null===(t=this._snapshot)||void 0===t?void 0:t.folders).sort(((e,t)=>e.name>t.name?1:-1)),this._addons=(i=null===(s=this._snapshot)||void 0===s?void 0:s.addons,i.map((e=>({slug:e.slug,name:e.name,version:e.version,checked:!0})))).sort(((e,t)=>e.name>t.name?1:-1)),this._dialogParams=e,this._onboarding=null!==(r=e.onboarding)&&void 0!==r&&r,this.supervisor=e.supervisor,this._snapshot.homeassistant||(this._restoreHass=!1)}},{kind:"method",key:"render",value:function(){return this._dialogParams&&this._snapshot?i.dy`
      <ha-dialog open @closing=${this._closeDialog} .heading=${!0}>
        <div slot="heading">
          <ha-header-bar>
            <span slot="title"> ${this._computeName} </span>
            <mwc-icon-button slot="actionItems" dialogAction="cancel">
              <ha-svg-icon .path=${r.r5M}></ha-svg-icon>
            </mwc-icon-button>
          </ha-header-bar>
        </div>
        <div class="details">
          ${"full"===this._snapshot.type?"Full snapshot":"Partial snapshot"}
          (${this._computeSize})<br />
          ${(0,o.o)(new Date(this._snapshot.date),this.hass.locale)}
        </div>
        ${this._snapshot.homeassistant?i.dy`<div>Home Assistant:</div>
              <paper-checkbox
                .checked=${this._restoreHass}
                @change="${e=>{this._restoreHass=e.target.checked}}"
              >
                Home Assistant
                <span class="version">(${this._snapshot.homeassistant})</span>
              </paper-checkbox>`:""}
        ${this._folders.length?i.dy`
              <div>Folders:</div>
              <paper-dialog-scrollable class="no-margin-top">
                ${this._folders.map((e=>i.dy`
                    <paper-checkbox
                      .checked=${e.checked}
                      @change="${t=>this._updateFolders(e,t.target.checked)}"
                    >
                      ${e.name}
                    </paper-checkbox>
                  `))}
              </paper-dialog-scrollable>
            `:""}
        ${this._addons.length?i.dy`
              <div>Add-on:</div>
              <paper-dialog-scrollable class="no-margin-top">
                ${this._addons.map((e=>i.dy`
                    <paper-checkbox
                      .checked=${e.checked}
                      @change="${t=>this._updateAddons(e,t.target.checked)}"
                    >
                      ${e.name}
                      <span class="version">(${e.version})</span>
                    </paper-checkbox>
                  `))}
              </paper-dialog-scrollable>
            `:""}
        ${this._snapshot.protected?i.dy`
              <paper-input
                autofocus=""
                label="Password"
                type="password"
                @value-changed=${this._passwordInput}
                .value=${this._snapshotPassword}
              ></paper-input>
            `:""}
        ${this._error?i.dy` <p class="error">Error: ${this._error}</p> `:""}

        <div class="button-row" slot="primaryAction">
          <mwc-button @click=${this._partialRestoreClicked}>
            <ha-svg-icon .path=${r.BBX} class="icon"></ha-svg-icon>
            Restore Selected
          </mwc-button>
          ${this._onboarding?"":i.dy`
                <mwc-button @click=${this._deleteClicked}>
                  <ha-svg-icon .path=${r.x9U} class="icon warning">
                  </ha-svg-icon>
                  <span class="warning">Delete Snapshot</span>
                </mwc-button>
              `}
        </div>
        <div class="button-row" slot="secondaryAction">
          ${"full"===this._snapshot.type?i.dy`
                <mwc-button @click=${this._fullRestoreClicked}>
                  <ha-svg-icon .path=${r.BBX} class="icon"></ha-svg-icon>
                  Restore Everything
                </mwc-button>
              `:""}
          ${this._onboarding?"":i.dy`<mwc-button @click=${this._downloadClicked}>
                <ha-svg-icon .path=${r.OGU} class="icon"></ha-svg-icon>
                Download Snapshot
              </mwc-button>`}
        </div>
      </ha-dialog>
    `:i.dy``}},{kind:"get",static:!0,key:"styles",value:function(){return[h.Qx,h.yu,i.iv`
        paper-checkbox {
          display: block;
          margin: 4px;
        }
        mwc-button ha-svg-icon {
          margin-right: 4px;
        }
        .button-row {
          display: grid;
          gap: 8px;
          margin-right: 8px;
        }
        .details {
          color: var(--secondary-text-color);
        }
        .warning,
        .error {
          color: var(--error-color);
        }
        .buttons li {
          list-style-type: none;
        }
        .buttons .icon {
          margin-right: 16px;
        }
        .no-margin-top {
          margin-top: 0;
        }
        span.version {
          color: var(--secondary-text-color);
        }
        ha-header-bar {
          --mdc-theme-on-primary: var(--primary-text-color);
          --mdc-theme-primary: var(--mdc-theme-surface);
          flex-shrink: 0;
        }
        /* overrule the ha-style-dialog max-height on small screens */
        @media all and (max-width: 450px), all and (max-height: 500px) {
          ha-header-bar {
            --mdc-theme-primary: var(--app-header-background-color);
            --mdc-theme-on-primary: var(--app-header-text-color, white);
          }
        }
      `]}},{kind:"method",key:"_updateFolders",value:function(e,t){this._folders=this._folders.map((s=>(s.slug===e.slug&&(s.checked=t),s)))}},{kind:"method",key:"_updateAddons",value:function(e,t){this._addons=this._addons.map((s=>(s.slug===e.slug&&(s.checked=t),s)))}},{kind:"method",key:"_passwordInput",value:function(e){this._snapshotPassword=e.detail.value}},{kind:"method",key:"_partialRestoreClicked",value:async function(){if(void 0!==this.supervisor&&"running"!==this.supervisor.info.state)return void await(0,d.Ys)(this,{title:"Could not restore snapshot",text:`Restoring a snapshot is not possible right now because the system is in ${this.supervisor.info.state} state.`});if(!await(0,d.g7)(this,{title:"Are you sure you want partially to restore this snapshot?",confirmText:"restore",dismissText:"cancel"}))return;const e=this._addons.filter((e=>e.checked)).map((e=>e.slug)),t=this._folders.filter((e=>e.checked)).map((e=>e.slug)),s={homeassistant:this._restoreHass,addons:e,folders:t};this._snapshot.protected&&(s.password=this._snapshotPassword),this._onboarding?((0,n.B)(this,"restoring"),fetch(`/api/hassio/snapshots/${this._snapshot.slug}/restore/partial`,{method:"POST",body:JSON.stringify(s)}),this._closeDialog()):this.hass.callApi("POST",`hassio/snapshots/${this._snapshot.slug}/restore/partial`,s).then((()=>{alert("Snapshot restored!"),this._closeDialog()}),(e=>{this._error=e.body.message}))}},{kind:"method",key:"_fullRestoreClicked",value:async function(){if(void 0!==this.supervisor&&"running"!==this.supervisor.info.state)return void await(0,d.Ys)(this,{title:"Could not restore snapshot",text:`Restoring a snapshot is not possible right now because the system is in ${this.supervisor.info.state} state.`});if(!await(0,d.g7)(this,{title:"Are you sure you want to wipe your system and restore this snapshot?",confirmText:"restore",dismissText:"cancel"}))return;const e=this._snapshot.protected?{password:this._snapshotPassword}:void 0;this._onboarding?((0,n.B)(this,"restoring"),fetch(`/api/hassio/snapshots/${this._snapshot.slug}/restore/full`,{method:"POST",body:JSON.stringify(e)}),this._closeDialog()):this.hass.callApi("POST",`hassio/snapshots/${this._snapshot.slug}/restore/full`,e).then((()=>{alert("Snapshot restored!"),this._closeDialog()}),(e=>{this._error=e.body.message}))}},{kind:"method",key:"_deleteClicked",value:async function(){await(0,d.g7)(this,{title:"Are you sure you want to delete this snapshot?",confirmText:"delete",dismissText:"cancel"})&&this.hass.callApi("POST",`hassio/snapshots/${this._snapshot.slug}/remove`).then((()=>{this._dialogParams.onDelete&&this._dialogParams.onDelete(),this._closeDialog()}),(e=>{this._error=e.body.message}))}},{kind:"method",key:"_downloadClicked",value:async function(){let e;try{e=await(0,a.iI)(this.hass,`/api/hassio/snapshots/${this._snapshot.slug}/download`)}catch(e){return void alert(`Error: ${(0,l.js)(e)}`)}if(window.location.href.includes("ui.nabu.casa")){if(!await(0,d.g7)(this,{title:"Potential slow download",text:"Downloading snapshots over the Nabu Casa URL will take some time, it is recomended to use your local URL instead, do you want to continue?",confirmText:"continue",dismissText:"cancel"}))return}const t=this._computeName.replace(/[^a-z0-9]+/gi,"_"),s=document.createElement("a");s.href=e.path,s.download=`Hass_io_${t}.tar`,this.shadowRoot.appendChild(s),s.click(),this.shadowRoot.removeChild(s)}},{kind:"get",key:"_computeName",value:function(){return this._snapshot?this._snapshot.name||this._snapshot.slug:"Unnamed snapshot"}},{kind:"get",key:"_computeSize",value:function(){return Math.ceil(10*this._snapshot.size)/10+" MB"}},{kind:"method",key:"_closeDialog",value:function(){this._dialogParams=void 0,this._snapshot=void 0,this._snapshotPassword="",this._folders=[],this._addons=[]}}]}}),i.oi)},43274:(e,t,s)=>{"use strict";s.d(t,{Sb:()=>r,BF:()=>i,Op:()=>o});const r=function(){try{(new Date).toLocaleDateString("i")}catch(e){return"RangeError"===e.name}return!1}(),i=function(){try{(new Date).toLocaleTimeString("i")}catch(e){return"RangeError"===e.name}return!1}(),o=function(){try{(new Date).toLocaleString("i")}catch(e){return"RangeError"===e.name}return!1}()},44583:(e,t,s)=>{"use strict";s.d(t,{o:()=>o,E:()=>n});var r=s(68928),i=s(43274);const o=i.Op?(e,t)=>e.toLocaleString(t.language,{year:"numeric",month:"long",day:"numeric",hour:"numeric",minute:"2-digit"}):e=>(0,r.WU)(e,"MMMM D, YYYY, HH:mm"),n=i.Op?(e,t)=>e.toLocaleString(t.language,{year:"numeric",month:"long",day:"numeric",hour:"numeric",minute:"2-digit",second:"2-digit"}):e=>(0,r.WU)(e,"MMMM D, YYYY, HH:mm:ss")}}]);
//# sourceMappingURL=chunk.224e17de5e7ae1810f00.js.map