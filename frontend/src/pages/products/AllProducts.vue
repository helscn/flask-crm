<template>
  <q-page class="q-gutter-md">
    <div class="q-gutter-md">
      <q-btn-group push>
        <q-btn push label="First" icon="timeline" @click="showDialog = true" />
        <q-btn push label="Second" icon="visibility" />
        <q-btn push label="Third" icon="update" />
      </q-btn-group>

      <q-dialog v-model="showDialog" persistent>
        <q-card>
          <q-form>
            <q-card-section class="q-gutter-md">
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
                <q-input
                  class="col-5"
                  filled
                  v-model="no"
                  label="产品编号*"
                  lazy-rules
                  :rules="[val => (val && val.length > 0) || '请输入产品编号']"
                />
                <q-input class="col-5" filled v-model="spec" label="产品规格" />
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
              <div class="row justify-between">
                <q-input
                  class="col-5"
                  filled
                  v-model="moq"
                  type="number"
                  label="最小采购量*"
                  lazy-rules
                  :rules="[val => val || '输入该产品的MOQ']"
                />
                <q-input
                  class="col-5"
                  filled
                  v-model="purchase_price"
                  type="number"
                  label="采购价格*"
                  prefix="¥"
                  lazy-rules
                  :rules="[val => val || '该产品的采购价格']"
                />
              </div>
              <div class="row justify-between">
                <q-input
                  class="col-5"
                  filled
                  v-model="refer_price"
                  type="number"
                  label="建议售价*"
                  prefix="$"
                  lazy-rules
                  :rules="[val => val > 0 || '建议的零售价格']"
                />
                <q-file
                  class="col-5"
                  v-model="thumbnail"
                  filled
                  label="产品缩略图"
                  accept=".jpg, image/*"
                  @rejected="onRejected"
                />
              </div>
            </q-card-section>
            <q-separator />
            <q-card-actions align="right">
              <q-btn
                v-close-popup
                flat
                color="primary"
                label="保存"
                @click="showDialog = false"
              />
              <q-btn
                v-close-popup
                flat
                color="primary"
                label="关闭"
                @click="showDialog = false"
              />
            </q-card-actions>
          </q-form>
        </q-card>
      </q-dialog>
    </div>
  </q-page>
</template>

<script>
export default {
  name: "AllProducts",
  data() {
    return {
      showDialog: false,
      no: "",
      name: "",
      spec: "",
      description: "",
      moq: 1,
      purchase_price: 1.0,
      refer_price: 1.0,
      comment: "",
      thumbnail: null
    };
  },
  methods: {
    add_product: function() {
      alert("ok");
      this.showCreateProduct = true;
    }
  }
};
</script>
