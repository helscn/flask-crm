<template>
  <q-page class="q-ma-xs q-mr-md q-pa-xs">
    <div class="q-py-lg row justify-center">
      <q-form
        ref="myForm"
        class="col-xs-12 col-sm-8 col-md-6 col-xl-4 shadow-3 q-pa-md q-gutter-xs"
      >
        <div class="row justify-between">
          <q-input
            class="col-5"
            filled
            v-model="no"
            label="产品编号*"
            lazy-rules
            :rules="[val => (val && val.length > 0) || '请输入产品编号']"
          />
          <q-file
            class="col-5"
            v-model="thumbnail"
            outlined
            label="产品缩略图"
            accept=".jpg, image/*"
          >
          </q-file>
        </div>
        <div class="row justify-between">
          <q-input
            class="col-12"
            filled
            v-model="name"
            label="产品名称*"
            lazy-rules
            :rules="[val => (val && val.length > 0) || '请输入产品名称']"
          />
        </div>
        <div class="row justify-between">
          <q-input class="col-5" filled v-model="spec" label="产品规格" />
          <q-input
            class="col-5"
            filled
            v-model="moq"
            label="最小采购量*"
            lazy-rules
            :rules="[val => val > 0 || '请输入最小采购量']"
          />
        </div>
        <div class="row justify-between">
          <q-input
            class="col-5"
            filled
            v-model="purchase_price"
            type="number"
            label="采购价格*"
            prefix="¥"
            lazy-rules
            :rules="[val => val > 0 || '请输入供应商采购价格']"
          />
          <q-input
            class="col-5"
            filled
            v-model="profit_rate"
            type="number"
            label="参考利润率"
            suffix="%"
            lazy-rules
            :rules="[val => val > 0 || '请输入参考利润率']"
          />
        </div>
        <div class="row justify-between">
          <q-input
            class="col-12"
            filled
            v-model="description"
            autogrow
            label="产品描述"
          />
        </div>
        <div class="row justify-around q-py-md">
          <q-btn color="primary" icon="save" label="保存" @click="test" />
          <q-btn color="primary" icon="cancel" label="取消" @click="cancel" />
        </div>
      </q-form>
    </div>
  </q-page>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "EditProduct",
  computed: {
    ...mapState({
      oldData(state) {
        return state.products.data.find(
          product => product.id == this.$route.query.id
        );
      }
    })
  },

  data() {
    let data = this.$store.state.products.data.find(
      product => product.id == this.$route.query.id
    );
    return {
      no: data.no,
      name: data.name,
      spec: data.spec,
      description: data.description,
      moq: data.moq,
      purchase_price: data.purchase_price,
      profit_rate: data.profit_rate,
      comment: data.comment,
      thumbnail: null
    };
  },
  methods: {
    test() {
      alert(this.id);
    },
    cancel() {
      this.$router.go(-1);
    },
    saveProduct() {
      this.$refs.myForm.validate().then(success => {
        if (success) {
          let form = new FormData();
          form.append("no", this.no);
          form.append("name", this.name);
          form.append("spec", this.spec);
          form.append("description", this.description);
          form.append("moq", this.moq);
          form.append("purchase_price", this.purchase_price);
          form.append("profit_rate", this.profit_rate / 100);
          form.append("comment", this.comment);
          form.append("thumbnail", this.thumbnail);
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
              this.$router.go(-1);
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
        } else {
          this.$q.notify({
            type: "negative",
            position: "top",
            icon: "error",
            message: "数据错误，请检查表单是否填写正确!",
            timeout: 1000
          });
        }
      });
    }
  },
  created: function() {
    this.$axios.get("/api/products/newno").then(res => {
      this.no = res.data.no;
    });
  }
};
</script>
