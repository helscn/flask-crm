<template>
  <div
    class="fullscreen text-white text-center q-pa-md flex flex-center"
    style="background: radial-gradient(circle, #35a2ff 0%, #014a88 100%)"
  >
    <div>
      <div class="text-h2 q-my-xl" style="opacity:.6">
        (๑ŐдŐ) 呃……该功能还未开发完成……
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
