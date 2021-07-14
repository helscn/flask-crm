<template>
  <q-page class="q-ma-xs q-mr-md q-pa-xs">
    <div class="q-py-lg row justify-center">
      <q-form
        ref="myForm"
        class="col-xs-12 col-sm-8 col-md-6 col-xl-4 shadow-3 q-pa-md"
      >
        <div class="row justify-between q-gutter-md">
          <div class="col q-mb-md">
            <q-input
              filled
              v-model="no"
              label="产品编号*"
              lazy-rules
              :rules="[val => (val && val.length > 0) || '请输入产品编号']"
            />
            <q-input
              filled
              v-model="name"
              label="产品名称*"
              lazy-rules
              :rules="[val => (val && val.length > 0) || '请输入产品名称']"
            />
            <q-select
              label="产品分类"
              filled
              v-model="category"
              use-input
              hide-dropdown-icon
              input-debounce="0"
              :options="categories"
            >
              <template v-if="category" v-slot:append>
                <q-icon
                  name="cancel"
                  @click.stop="category = null"
                  class="cursor-pointer"
                />
              </template>
            </q-select>
          </div>
          <div class="col q-mb-md" style="border:1px solid #c2c2c2">
            <q-file
              v-model="thumbnail"
              outlined
              label="产品缩略图"
              accept=".jpg, image/*"
            />
            <q-img :src="thumbnail_file" />
          </div>
        </div>
        <div class="row justify-between q-gutter-md">
          <q-input class="col" filled v-model="spec" label="产品规格" />
          <q-input
            class="col"
            filled
            v-model="moq"
            label="最小采购量*"
            lazy-rules
            :rules="[val => val > 0 || '请输入最小采购量']"
          />
        </div>
        <div class="row justify-between q-gutter-md">
          <q-input
            class="col"
            filled
            v-model="purchase_price"
            type="number"
            label="采购价格*"
            prefix="¥"
            lazy-rules
            :rules="[val => val > 0 || '请输入供应商采购价格']"
          />
          <q-input
            class="col"
            filled
            v-model="profit_rate"
            type="number"
            label="参考利润率"
            suffix="%"
            lazy-rules
            :rules="[val => val > 0 || '请输入参考利润率']"
          >
            <q-tooltip>
              参考售价 ${{
                ((purchase_price * (1 + profit_rate / 100)) / 6.6).toFixed(2)
              }}
            </q-tooltip>
          </q-input>
        </div>
        <div class="row justify-between q-gutter-md">
          <q-input
            class="col"
            filled
            v-model="description"
            autogrow
            label="产品描述"
          />
        </div>
        <div class="row justify-around q-pt-md">
          <q-btn
            color="primary"
            icon="save"
            label="保存"
            @click="saveProduct"
          />
          <q-btn color="primary" icon="cancel" label="取消" @click="cancel" />
        </div>
      </q-form>
    </div>
  </q-page>
</template>

<script>
export default {
  name: "CreateProduct",
  data() {
    return {
      no: "",
      name: "",
      spec: "",
      description: "",
      moq: 100,
      purchase_price: 1.0,
      profit_rate: 15,
      comment: "",
      thumbnail: null,
      thumbnail_file: null,
      category: null,
      categories: []
    };
  },
  watch: {
    thumbnail: function(val, oldVal) {
      this.thumbnail_file = window.URL.createObjectURL(val);
    }
  },
  methods: {
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
