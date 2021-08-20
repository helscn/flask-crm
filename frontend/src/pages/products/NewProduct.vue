<template>
  <q-page class="q-ma-xs q-mr-md q-pa-xs">
    <ProductEditer :form-data="product" newno @save="save" @cancel="cancel" />
  </q-page>
</template>

<script>
import ProductEditer from "components/ProductEditer.vue";

export default {
  name: "CreateProduct",
  components: { ProductEditer },
  data() {
    return {
      product: null
    };
  },
  methods: {
    cancel() {
      this.$router.go(-1);
    },
    save(form) {
      let config = {
        headers: {
          "Content-Type": "multipart/form-data"
        }
      };
      this.$axios
        .post("/api/products", form, config)
        .then(res => {
          this.$q.notify({
            type: "positive",
            position: "top",
            icon: "check_circle",
            message: "产品保存成功。",
            timeout: 1000
          });
          this.$store.dispatch("products/fetchProducts");
          this.$router.push("/products");
        })
        .catch(error => {
          this.$q.notify({
            type: "negative",
            position: "top",
            icon: "error",
            message: "保存产品出错，请检查网络连接是否正常。",
            timeout: 1000
          });
        });
    }
  },
  created: function() {
    this.$axios.get("/api/products/newno").then(res => {
      this.product = { no: res.data.no };
    });
  }
};
</script>
