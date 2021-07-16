<template>
  <q-page class="q-ma-xs q-mr-md q-pa-xs">
    <SupplierEditer :form-data="supplier" newno @save="save" @cancel="cancel" />
  </q-page>
</template>

<script>
import SupplierEditer from "components/SupplierEditer.vue";

export default {
  name: "NewSupplier",
  components: { SupplierEditer },
  data() {
    return {
      supplier: null
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
        .post("/api/products/suppliers", form, config)
        .then(res => {
          this.$q.notify({
            type: "positive",
            position: "top",
            icon: "check_circle",
            message: "供应商信息保存成功。",
            timeout: 1000
          });
          this.$store.dispatch("products/fetchSuppliers");
          this.$router.go(-1);
        })
        .catch(error => {
          this.$q.notify({
            type: "negative",
            position: "top",
            icon: "error",
            message: "保存信息出错，请检查网络连接是否正常。",
            timeout: 1000
          });
        });
    }
  }
};
</script>
