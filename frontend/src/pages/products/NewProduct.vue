<template>
  <q-page class="q-ma-xs q-mr-md q-pa-xs q-gutter-md flex">
    <q-form style="max-width: 400px">
      <q-input
        filled
        v-model="no"
        label="产品编号"
        hint="Name and surname"
        lazy-rules
        :rules="[val => (val && val.length > 0) || 'Please type something']"
      />
      <q-input
        filled
        v-model="name"
        label="产品名称*"
        hint="Name and surname"
        lazy-rules
        :rules="[val => (val && val.length > 0) || 'Please type something']"
      />
      <q-input
        filled
        v-model="spec"
        label="产品规格"
        hint="Name and surname"
        lazy-rules
        :rules="[val => (val && val.length > 0) || 'Please type something']"
      />
      <q-input
        filled
        v-model="description"
        label="产品描述"
        hint="Name and surname"
        lazy-rules
        :rules="[val => (val && val.length > 0) || 'Please type something']"
      />
      <q-input
        filled
        v-model="moq"
        label="最小采购量*"
        hint="Name and surname"
        lazy-rules
        :rules="[val => (val => val > 0) || '请输入最小采购量']"
      />
      <q-input
        filled
        v-model="purchase_price"
        type="number"
        label="采购价格*"
        hint="Name and surname"
        prefix="¥"
        lazy-rules
        :rules="[val => val > 0 || '请输入商采购价格']"
      />
      <q-input
        filled
        v-model="profit_rate"
        type="number"
        label="参考利润率"
        hint="Name and surname"
        suffix="%"
        lazy-rules
        :rules="[val => (val && val.length > 0) || 'Please type something']"
      />
      <q-file
        style="max-width: 300px"
        v-model="thumbnail"
        filled
        label="产品缩略图"
        accept=".jpg, image/*"
      />
    </q-form>
  </q-page>
</template>

<script>
export default {
  name: "CreateProduct",
  data() {
    return {
      showCreateProduct: true,
      no: "",
      name: "",
      spec: "",
      description: "",
      moq: 100,
      purchase_price: 0.0,
      profit_rate: 0.0,
      comment: "",
      thumbnail: null
    };
  }
};
</script>
