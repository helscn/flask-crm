<template>
  <div class="q-py-lg row justify-center">
    <q-form
      ref="myForm"
      class="col-xs-12 col-sm-8 col-md-6 col-xl-4 shadow-3 q-pa-md q-gutter-md"
    >
      <div class="row justify-between q-gutter-md">
        <q-input
          class="col"
          filled
          v-model.trim="name"
          label="供应商名称*"
          lazy-rules
          :rules="[val => (val && val.length > 0) || '请输入供应商的名称']"
        />
        <q-input class="col" filled v-model.trim="contract" label="联系人" />
      </div>
      <div class="row justify-between q-gutter-md">
        <q-input class="col" filled v-model.trim="email" label="邮箱" />
        <q-input class="col" filled v-model.trim="phone" label="电话" />
      </div>
      <div class="row justify-between q-gutter-md">
        <q-input class="col" filled v-model.trim="website" label="网站" />
      </div>
      <div class="row justify-between q-gutter-md">
        <q-input class="col" filled v-model.trim="address" label="地址" />
      </div>
      <div class="row justify-between q-gutter-md">
        <q-input
          class="col"
          filled
          v-model="comment"
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
  name: "SupplierEditor",
  props: {
    formData: Object
  },
  data() {
    return {
      id: null,
      name: "",
      contract: "",
      email: "",
      phone: "",
      address: "",
      website: "",
      comment: ""
    };
  },
  watch: {
    formData: {
      handler: function(val, oldval) {
        if (val) {
          this.id = val.id || this.id;
          this.name = val.name || this.name;
          this.contract = val.contract || this.contract;
          this.email = val.email || this.email;
          this.phone = val.phone || this.phone;
          this.address = val.address || this.address;
          this.website = val.website || this.website;
          this.comment = val.comment || this.comment;
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
          form.append("name", this.name);
          form.append("contract", this.contract);
          form.append("email", this.email);
          form.append("phone", this.phone);
          form.append("address", this.address);
          form.append("website", this.website);
          form.append("comment", this.comment);
          form.append("comment", this.comment);
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
  }
};
</script>
