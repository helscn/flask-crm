<template>
  <div class="q-py-lg row justify-center">
    <q-form
      ref="myForm"
      class="col-xs-12 col-sm-8 col-md-6 col-xl-4 shadow-3 q-pa-md"
    >
      <div class="row justify-between q-gutter-md">
        <q-input
          class="col"
          filled
          v-model="no"
          label="产品编号*"
          lazy-rules
          :rules="[val => (val && val.length > 0) || '请输入产品编号']"
        />
        <q-select
          class="col"
          label="供应商"
          filled
          v-model="category"
          use-input
          hide-dropdown-icon
          input-debounce="0"
          :options="categories"
        />
      </div>
      <div class="row justify-between q-gutter-md">
        <div class="col q-mb-md">
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
          <q-img :src="thumbnail_url" />
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
        <q-btn color="primary" icon="save" label="保存" @click="save" />
        <q-btn color="primary" icon="cancel" label="取消" @click="cancel" />
      </div>
    </q-form>
  </div>
</template>

<script>
export default {
  name: "ProductEditer",
  props: {
    formData: Object
  },
  data() {
    return {
      id: null,
      no: "",
      name: "",
      spec: "",
      description: "",
      moq: 0,
      purchase_price: 0.0,
      profit_rate: 0.0,
      comment: "",
      thumbnail: null,
      thumbnail_url: null,
      supplier: null,
      suppliers: [],
      category: null,
      categories: []
    };
  },
  watch: {
    thumbnail: function(val, oldVal) {
      this.thumbnail_url = window.URL.createObjectURL(val);
    },
    formData: {
      handler: function(val, oldval) {
        if (val) {
          this.id = val.id || this.id;
          this.no = val.no || this.no;
          this.name = val.name || this.name;
          this.description = val.description || this.description;
          this.moq = val.moq || this.moq;
          this.purchase_price = val.purchase_price || this.purchase_price;
          this.profit_rate = val.profit_rate * 100 || this.profit_rate;
          this.comment = val.comment || this.comment;
          this.supplier = val.supplier || this.supplier;
          this.category = val.category || this.category;
          this.thumbnail_url = val.thumbnail || this.thumbnail_url;
        }
      },
      immediate: true
    }
  },
  methods: {
    cancel() {
      this.$emit("cancel");
    },
    save() {
      this.$refs.myForm.validate().then(success => {
        if (success) {
          let form = new FormData();
          form.append("id", this.id);
          form.append("no", this.no);
          form.append("name", this.name);
          form.append("spec", this.spec);
          form.append("description", this.description);
          form.append("moq", this.moq);
          form.append("purchase_price", this.purchase_price);
          form.append("profit_rate", this.profit_rate / 100);
          form.append("comment", this.comment);
          form.append("supplier", this.supplier);
          form.append("category", this.category);
          form.append("thumbnail", this.thumbnail);
          this.$emit("save", form, this.id);
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
    this.$store.dispatch("products/fetchCategories").then(res => {
      this.categories = this.$store.getters["products/productCategories"];
    });
  }
};
</script>
