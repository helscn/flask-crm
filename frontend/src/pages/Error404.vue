<template>
  <div
    class="fullscreen bg-blue text-white text-center q-pa-md flex flex-center"
  >
    <div>
      <div style="font-size: 30vh">
        404
      </div>

      <div class="text-h2" style="opacity:.4">
        Oops. Nothing here...
      </div>
      <div class="q-gutter-md">
        <q-btn
          class="q-mt-xl"
          color="white"
          text-color="blue"
          unelevated
          @click="go_back"
          label="返回"
          icon="arrow_back"
          no-caps
        />
        <q-btn
          class="q-mt-xl"
          color="white"
          text-color="blue"
          unelevated
          to="/"
          label="主页"
          icon="home"
          no-caps
        />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Error404",
  methods: {
    go_back: function() {
      this.$router.go(-1);
    }
  }
};
</script>
