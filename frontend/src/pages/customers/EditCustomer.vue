<template>
  <q-page class="q-ma-xs q-mr-md q-pa-xs">
    <CustomerEditer :data="customer" @save="save" @cancel="cancel" />
  </q-page>
</template>

<script>
import CustomerEditer from "components/CustomerEditer.vue";

export default {
  name: "EditCustomer",
  components: { CustomerEditer },
  data() {
    return {
      customer: null
    };
  },

  methods: {
    cancel() {
      this.$router.go(-1);
    },
    save(data) {
      this.$axios
        .put("/api/customers", data)
        .then(res => {
          this.$q.notify({
            type: "positive",
            position: "top",
            icon: "check_circle",
            message: "客户信息保存成功。",
            timeout: 1000
          });
          this.$store.dispatch("customers/fetchCustomers");
          this.$router.go(-1);
        })
        .catch(error => {
          this.$q.notify({
            type: "negative",
            position: "top",
            icon: "error",
            message: "保存客户信息出错，请检查网络连接是否正常。",
            timeout: 1000
          });
        });
    }
  },
  created: function() {
    this.$axios
      .get("/api/customers/" + this.$route.query.id)
      .then(({ data }) => {
        this.customer = data;
      });
  }
};
</script>
