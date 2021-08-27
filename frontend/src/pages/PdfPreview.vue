<template>
  <q-layout>
    <q-page-container>
      <q-page class="flex flex-center">
        <img alt="DTN-Tech logo" src="~assets/logo.png" />
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script>
console.log("Loading js library...");
let $ = require("assets/js/jquery.min.js");
let polyfill = require("assets/js/polyfill.min.js");
let lodash = require("assets/js/lodash.min.js");
let bookjs = require("assets/js/bookjs-eazy.min.js");

console.log("Js library loaded.");

export default {
  name: "PdfPreview",
  created: function() {
    console.log("Page Created.");
  },
  mounted: function() {
    console.log("Page mounted.");
  }
};
</script>
