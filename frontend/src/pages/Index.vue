<template>
  <q-page class="flex flex-center">
    <img
      @click="test"
      alt="Quasar logo"
      src="~assets/quasar-logo-vertical.svg"
      style="width: 200px; height: 200px"
    />
  </q-page>
</template>

<script>
export default {
  name: "PageIndex",
  methods: {
    test: function() {}
  }
};
</script>
