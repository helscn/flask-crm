<template>
  <q-page class="flex flex-center">
    <div class="q-pa-md">
      <div class="q-gutter-sm row items-start">
        <q-uploader
          label="Individual upload"
          :factory="upload"
          multiple
          style="max-width: 300px"
        />

        <q-uploader
          url="/api/files"
          label="Batch upload"
          multiple
          batch
          style="max-width: 300px"
        />
      </div>
    </div>
  </q-page>
</template>

<script>
export default {
  name: "Upload",
  methods: {
    upload: function(files) {
      const token = localStorage.getItem("Token");
      return {
        url: "http://localhost:5000/api/files",
        method: "POST",
        headers: [{ name: "Token", value: token }]
      };
    }
  }
};
</script>
