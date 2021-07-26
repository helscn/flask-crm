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
          v-model.trim="no"
          label="产品编号*"
          lazy-rules
          :rules="[val => (val && val.length > 0) || '请输入产品编号']"
        />
        <q-select
          class="col"
          label="供应商"
          clearable
          filled
          v-model.trim="supplier"
          use-input
          input-debounce="0"
          bottom-slots
          @filter="suppliersFilter"
          :options="suppliers"
        >
          <template v-slot:no-option>
            <q-item>
              <q-item-section class="text-grey">
                找不到对应供应商
              </q-item-section>
            </q-item>
          </template>
          <template v-slot:append>
            <q-icon
              name="add_circle"
              @click="addSupplier"
              class="cursor-pointer"
            >
              <q-tooltip>
                添加产品供应商
              </q-tooltip>
            </q-icon>
          </template>
        </q-select>
      </div>
      <div class="row justify-between q-gutter-md">
        <div class="col q-mb-md">
          <q-input
            filled
            v-model.trim="name"
            label="产品名称*"
            lazy-rules
            :rules="[val => (val && val.length > 0) || '请输入产品名称']"
          />
          <q-select
            label="产品分类"
            clearable
            filled
            v-model.trim="category"
            use-input
            input-debounce="0"
            bottom-slots
            @filter="categoriesFilter"
            :options="categories"
          >
            <template v-slot:no-option>
              <q-item>
                <q-item-section class="text-grey">
                  找不到对应产品分类
                </q-item-section>
              </q-item>
            </template>
            <template v-slot:append>
              <q-icon
                name="add_circle"
                @click.stop="isShowDialog = true"
                class="cursor-pointer"
              >
                <q-tooltip>
                  添加产品分类
                </q-tooltip>
              </q-icon>
            </template>
          </q-select>
          <q-select label="单位" filled v-model="unit" :options="units" />
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
          mask="#.##"
          fill-mask="0"
          reverse-fill-mask
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
    <q-dialog v-model="isShowDialog" persistent>
      <q-card style="min-width: 350px">
        <q-card-section>
          <div class="text-subtitle1">请输入新产品类别名称：</div>
        </q-card-section>

        <q-card-section class="q-pt-none">
          <q-input
            dense
            v-model.trim="newCategory"
            autofocus
            @keyup.enter="saveCategory"
            @keyup.esc="closeDialog"
          />
        </q-card-section>

        <q-card-actions align="right" class="text-primary">
          <q-btn flat label="取消" v-close-popup @click="closeDialog" />
          <q-btn flat label="保存" v-close-popup @click="saveCategory" />
        </q-card-actions>
      </q-card>
    </q-dialog>
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
      id: 0,
      no: "",
      name: "",
      spec: "",
      description: "",
      moq: 100,
      purchase_price: "1.00",
      profit_rate: 15.0,
      thumbnail: null,
      thumbnail_url: null,
      unit: "pcs",
      units: ["pcs", "set"],
      supplier: null,
      suppliers: [],
      category: null,
      categories: [],
      isShowDialog: false,
      newCategory: ""
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
          this.spec = val.spec || this.spec;
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
          form.append("unit", this.unit);
          form.append("description", this.description);
          form.append("moq", this.moq);
          form.append("purchase_price", this.purchase_price);
          form.append("profit_rate", this.profit_rate / 100);
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
    },
    suppliersFilter(val, update, abort) {
      update(() => {
        const keyword = val.toLowerCase();
        const suppliers = this.$store.getters["products/productSuppliers"];
        this.suppliers = suppliers.filter(
          v => v.toLowerCase().indexOf(keyword) > -1
        );
      });
    },
    categoriesFilter(val, update, abort) {
      update(() => {
        const keyword = val.toLowerCase();
        const categories = this.$store.getters["products/productCategories"];
        this.categories = categories.filter(
          v => v.toLowerCase().indexOf(keyword) > -1
        );
      });
    },
    addSupplier() {
      this.$router.push("/suppliers/new");
    },
    closeDialog() {
      this.isShowDialog = false;
      this.newCategory = "";
    },
    saveCategory() {
      if (this.categories.indexOf(this.newCategory) === -1) {
        this.$axios
          .post("/api/products/categories", {
            name: this.newCategory
          })
          .then(res => {
            this.$store.dispatch("products/fetchCategories").then(res => {
              this.cateogry = this.newCategory;
              this.$q.notify({
                type: "positive",
                position: "top",
                icon: "check_circle",
                message: "已新建产品分类：" + this.newCategory,
                timeout: 1000
              });
            });
          })
          .catch(err => {
            this.$q.notify({
              type: "negative",
              position: "top",
              icon: "error",
              message: "保存产品类别信息出错，请检查网络连接是否正常!",
              timeout: 1000
            });
          });
      } else {
        this.$q.notify({
          type: "negative",
          position: "top",
          icon: "error",
          message: "输入的产品类别重复!",
          timeout: 1000
        });
        this.newCategory = "";
      }
    }
  },
  created: function() {
    this.$store.dispatch("products/fetchCategories").then(res => {
      this.categories = this.$store.getters["products/productCategories"];
    });
    this.$store.dispatch("products/fetchSuppliers").then(res => {
      this.suppliers = this.$store.getters["products/productSuppliers"];
    });
  }
};
</script>
