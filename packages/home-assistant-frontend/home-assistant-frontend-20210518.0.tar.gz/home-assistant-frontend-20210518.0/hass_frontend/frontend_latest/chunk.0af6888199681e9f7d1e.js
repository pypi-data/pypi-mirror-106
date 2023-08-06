/*! For license information please see chunk.0af6888199681e9f7d1e.js.LICENSE.txt */
(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[4651],{35854:(e,r,t)=>{"use strict";t.d(r,{G:()=>i,R:()=>o});t(65233);var a=t(21006),c=t(98235);const i={properties:{checked:{type:Boolean,value:!1,reflectToAttribute:!0,notify:!0,observer:"_checkedChanged"},toggles:{type:Boolean,value:!0,reflectToAttribute:!0},value:{type:String,value:"on",observer:"_valueChanged"}},observers:["_requiredChanged(required)"],created:function(){this._hasIronCheckedElementBehavior=!0},_getValidity:function(e){return this.disabled||!this.required||this.checked},_requiredChanged:function(){this.required?this.setAttribute("aria-required","true"):this.removeAttribute("aria-required")},_checkedChanged:function(){this.active=this.checked,this.fire("iron-change")},_valueChanged:function(){void 0!==this.value&&null!==this.value||(this.value="on")}},o=[a.V,c.x,i]},62132:(e,r,t)=>{"use strict";t.d(r,{K:()=>n});t(65233);var a=t(35854),c=t(49075),i=t(84938);const o={_checkedChanged:function(){a.G._checkedChanged.call(this),this.hasRipple()&&(this.checked?this._ripple.setAttribute("checked",""):this._ripple.removeAttribute("checked"))},_buttonStateChanged:function(){i.o._buttonStateChanged.call(this),this.disabled||this.isAttached&&(this.checked=this.active)}},n=[c.B,a.R,o]},32296:(e,r,t)=>{"use strict";t(65233);var a=t(62132),c=t(49075),i=t(9672),o=t(50856),n=t(87529);const l=o.d`<style>
  :host {
    display: inline-block;
    white-space: nowrap;
    cursor: pointer;
    --calculated-paper-checkbox-size: var(--paper-checkbox-size, 18px);
    /* -1px is a sentinel for the default and is replaced in \`attached\`. */
    --calculated-paper-checkbox-ink-size: var(--paper-checkbox-ink-size, -1px);
    @apply --paper-font-common-base;
    line-height: 0;
    -webkit-tap-highlight-color: transparent;
  }

  :host([hidden]) {
    display: none !important;
  }

  :host(:focus) {
    outline: none;
  }

  .hidden {
    display: none;
  }

  #checkboxContainer {
    display: inline-block;
    position: relative;
    width: var(--calculated-paper-checkbox-size);
    height: var(--calculated-paper-checkbox-size);
    min-width: var(--calculated-paper-checkbox-size);
    margin: var(--paper-checkbox-margin, initial);
    vertical-align: var(--paper-checkbox-vertical-align, middle);
    background-color: var(--paper-checkbox-unchecked-background-color, transparent);
  }

  #ink {
    position: absolute;

    /* Center the ripple in the checkbox by negative offsetting it by
     * (inkWidth - rippleWidth) / 2 */
    top: calc(0px - (var(--calculated-paper-checkbox-ink-size) - var(--calculated-paper-checkbox-size)) / 2);
    left: calc(0px - (var(--calculated-paper-checkbox-ink-size) - var(--calculated-paper-checkbox-size)) / 2);
    width: var(--calculated-paper-checkbox-ink-size);
    height: var(--calculated-paper-checkbox-ink-size);
    color: var(--paper-checkbox-unchecked-ink-color, var(--primary-text-color));
    opacity: 0.6;
    pointer-events: none;
  }

  #ink:dir(rtl) {
    right: calc(0px - (var(--calculated-paper-checkbox-ink-size) - var(--calculated-paper-checkbox-size)) / 2);
    left: auto;
  }

  #ink[checked] {
    color: var(--paper-checkbox-checked-ink-color, var(--primary-color));
  }

  #checkbox {
    position: relative;
    box-sizing: border-box;
    height: 100%;
    border: solid 2px;
    border-color: var(--paper-checkbox-unchecked-color, var(--primary-text-color));
    border-radius: 2px;
    pointer-events: none;
    -webkit-transition: background-color 140ms, border-color 140ms;
    transition: background-color 140ms, border-color 140ms;

    -webkit-transition-duration: var(--paper-checkbox-animation-duration, 140ms);
    transition-duration: var(--paper-checkbox-animation-duration, 140ms);
  }

  /* checkbox checked animations */
  #checkbox.checked #checkmark {
    -webkit-animation: checkmark-expand 140ms ease-out forwards;
    animation: checkmark-expand 140ms ease-out forwards;

    -webkit-animation-duration: var(--paper-checkbox-animation-duration, 140ms);
    animation-duration: var(--paper-checkbox-animation-duration, 140ms);
  }

  @-webkit-keyframes checkmark-expand {
    0% {
      -webkit-transform: scale(0, 0) rotate(45deg);
    }
    100% {
      -webkit-transform: scale(1, 1) rotate(45deg);
    }
  }

  @keyframes checkmark-expand {
    0% {
      transform: scale(0, 0) rotate(45deg);
    }
    100% {
      transform: scale(1, 1) rotate(45deg);
    }
  }

  #checkbox.checked {
    background-color: var(--paper-checkbox-checked-color, var(--primary-color));
    border-color: var(--paper-checkbox-checked-color, var(--primary-color));
  }

  #checkmark {
    position: absolute;
    width: 36%;
    height: 70%;
    border-style: solid;
    border-top: none;
    border-left: none;
    border-right-width: calc(2/15 * var(--calculated-paper-checkbox-size));
    border-bottom-width: calc(2/15 * var(--calculated-paper-checkbox-size));
    border-color: var(--paper-checkbox-checkmark-color, white);
    -webkit-transform-origin: 97% 86%;
    transform-origin: 97% 86%;
    box-sizing: content-box; /* protect against page-level box-sizing */
  }

  #checkmark:dir(rtl) {
    -webkit-transform-origin: 50% 14%;
    transform-origin: 50% 14%;
  }

  /* label */
  #checkboxLabel {
    position: relative;
    display: inline-block;
    vertical-align: middle;
    padding-left: var(--paper-checkbox-label-spacing, 8px);
    white-space: normal;
    line-height: normal;
    color: var(--paper-checkbox-label-color, var(--primary-text-color));
    @apply --paper-checkbox-label;
  }

  :host([checked]) #checkboxLabel {
    color: var(--paper-checkbox-label-checked-color, var(--paper-checkbox-label-color, var(--primary-text-color)));
    @apply --paper-checkbox-label-checked;
  }

  #checkboxLabel:dir(rtl) {
    padding-right: var(--paper-checkbox-label-spacing, 8px);
    padding-left: 0;
  }

  #checkboxLabel[hidden] {
    display: none;
  }

  /* disabled state */

  :host([disabled]) #checkbox {
    opacity: 0.5;
    border-color: var(--paper-checkbox-unchecked-color, var(--primary-text-color));
  }

  :host([disabled][checked]) #checkbox {
    background-color: var(--paper-checkbox-unchecked-color, var(--primary-text-color));
    opacity: 0.5;
  }

  :host([disabled]) #checkboxLabel  {
    opacity: 0.65;
  }

  /* invalid state */
  #checkbox.invalid:not(.checked) {
    border-color: var(--paper-checkbox-error-color, var(--error-color));
  }
</style>

<div id="checkboxContainer">
  <div id="checkbox" class$="[[_computeCheckboxClass(checked, invalid)]]">
    <div id="checkmark" class$="[[_computeCheckmarkClass(checked)]]"></div>
  </div>
</div>

<div id="checkboxLabel"><slot></slot></div>`;l.setAttribute("strip-whitespace",""),(0,i.k)({_template:l,is:"paper-checkbox",behaviors:[a.K],hostAttributes:{role:"checkbox","aria-checked":!1,tabindex:0},properties:{ariaActiveAttribute:{type:String,value:"aria-checked"}},attached:function(){(0,n.T8)(this,(function(){if("-1px"===this.getComputedStyleValue("--calculated-paper-checkbox-ink-size").trim()){var e=this.getComputedStyleValue("--calculated-paper-checkbox-size").trim(),r="px",t=e.match(/[A-Za-z]+$/);null!==t&&(r=t[0]);var a=parseFloat(e),c=8/3*a;"px"===r&&(c=Math.floor(c))%2!=a%2&&c++,this.updateStyles({"--paper-checkbox-ink-size":c+r})}}))},_computeCheckboxClass:function(e,r){var t="";return e&&(t+="checked "),r&&(t+="invalid"),t},_computeCheckmarkClass:function(e){return e?"":"hidden"},_createRipple:function(){return this._rippleContainer=this.$.checkboxContainer,c.S._createRipple.call(this)}})},57724:(e,r,t)=>{"use strict";t.d(r,{E_:()=>u,i9:()=>k,_Y:()=>s,pt:()=>i,OR:()=>n,hN:()=>o,ws:()=>b,fk:()=>h,hl:()=>p});var a=t(99602);const{et:c}=a.Vm,i=e=>null===e||"object"!=typeof e&&"function"!=typeof e,o=(e,r)=>{var t,a;return void 0===r?void 0!==(null===(t=e)||void 0===t?void 0:t._$litType$):(null===(a=e)||void 0===a?void 0:a._$litType$)===r},n=e=>void 0===e.strings,l=()=>document.createComment(""),s=(e,r,t)=>{var a;const i=e.A.parentNode,o=void 0===r?e.B:r.A;if(void 0===t){const r=i.insertBefore(l(),o),a=i.insertBefore(l(),o);t=new c(r,a,e,e.options)}else{const r=t.B.nextSibling,c=t.M!==e;if(c&&(null===(a=t.Q)||void 0===a||a.call(t,e),t.M=e),r!==o||c){let e=t.A;for(;e!==r;){const r=e.nextSibling;i.insertBefore(e,o),e=r}}}return t},h=(e,r,t=e)=>(e.I(r,t),e),d={},p=(e,r=d)=>e.H=r,k=e=>e.H,b=e=>{var r;null===(r=e.P)||void 0===r||r.call(e,!1,!0);let t=e.A;const a=e.B.nextSibling;for(;t!==a;){const e=t.nextSibling;t.remove(),t=e}},u=e=>{e.R()}},40417:(e,r,t)=>{"use strict";t.d(r,{l:()=>o});var a=t(99602),c=t(55122);const i={},o=(0,c.XM)(class extends c.Xe{constructor(){super(...arguments),this.$t=i}render(e,r){return r()}update(e,[r,t]){if(Array.isArray(r)){if(Array.isArray(this.$t)&&this.$t.length===r.length&&r.every(((e,r)=>e===this.$t[r])))return a.Jb}else if(this.$t===r)return a.Jb;return this.$t=Array.isArray(r)?Array.from(r):r,this.render(r,t)}})},13690:(e,r,t)=>{"use strict";t.d(r,{r:()=>n});var a=t(99602),c=t(55122),i=t(57724);const o=(e,r,t)=>{const a=new Map;for(let c=r;c<=t;c++)a.set(e[c],c);return a},n=(0,c.XM)(class extends c.Xe{constructor(e){if(super(e),e.type!==c.pX.CHILD)throw Error("repeat() can only be used in text expressions")}Mt(e,r,t){let a;void 0===t?t=r:void 0!==r&&(a=r);const c=[],i=[];let o=0;for(const r of e)c[o]=a?a(r,o):o,i[o]=t(r,o),o++;return{values:i,keys:c}}render(e,r,t){return this.Mt(e,r,t).values}update(e,[r,t,c]){var n;const l=(0,i.i9)(e),{values:s,keys:h}=this.Mt(r,t,c);if(!l)return this.Pt=h,s;const d=null!==(n=this.Pt)&&void 0!==n?n:this.Pt=[],p=[];let k,b,u=0,v=l.length-1,x=0,f=s.length-1;for(;u<=v&&x<=f;)if(null===l[u])u++;else if(null===l[v])v--;else if(d[u]===h[x])p[x]=(0,i.fk)(l[u],s[x]),u++,x++;else if(d[v]===h[f])p[f]=(0,i.fk)(l[v],s[f]),v--,f--;else if(d[u]===h[f])p[f]=(0,i.fk)(l[u],s[f]),(0,i._Y)(e,p[f+1],l[u]),u++,f--;else if(d[v]===h[x])p[x]=(0,i.fk)(l[v],s[x]),(0,i._Y)(e,l[u],l[v]),v--,x++;else if(void 0===k&&(k=o(h,x,f),b=o(d,u,v)),k.has(d[u]))if(k.has(d[v])){const r=b.get(h[x]),t=void 0!==r?l[r]:null;if(null===t){const r=(0,i._Y)(e,l[u]);(0,i.fk)(r,s[x]),p[x]=r}else p[x]=(0,i.fk)(t,s[x]),(0,i._Y)(e,l[u],t),l[r]=null;x++}else(0,i.ws)(l[v]),v--;else(0,i.ws)(l[u]),u++;for(;x<=f;){const r=(0,i._Y)(e,p[f+1]);(0,i.fk)(r,s[x]),p[x++]=r}for(;u<=v;){const e=l[u++];null!==e&&(0,i.ws)(e)}return this.Pt=h,(0,i.hl)(e,p),a.Jb}})}}]);
//# sourceMappingURL=chunk.0af6888199681e9f7d1e.js.map