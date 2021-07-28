<template>
  <q-page class="q-ma-xs q-mr-md q-pa-xs q-gutter-md">
    <template>
      <q-btn-group rounded push>
        <q-btn
          label="新建"
          icon="add_circle_outline"
          @click="$router.push('/suppliers/new')"
          color="primary"
        />
        <q-btn
          label="修改"
          :disable="selected.length !== 1"
          icon="edit"
          @click="
            $router.push({
              path: '/suppliers/edit',
              query: { id: selected[0].id }
            })
          "
          color="primary"
        />
        <q-btn
          label="删除"
          :disable="selected.length === 0"
          rounded
          icon="delete_forever"
          @click="removeSuppliers"
          color="primary"
        />
      </q-btn-group>
      <q-btn-group rounded>
        <q-btn
          label="导出"
          icon="file_download"
          @click="$router.push('/suppliers/download')"
          color="primary"
        />
        <q-btn
          label="导入"
          icon="file_upload"
          @click="$router.push('/suppliers/upload')"
          color="primary"
        />
      </q-btn-group>
    </template>
    <q-table
      ref="suppliersTable"
      :loading="loading"
      :data="data"
      :columns="columns"
      row-key="id"
      selection="multiple"
      :selected.sync="selected"
      :pagination.sync="pagination"
      :filter="filter"
      :visible-columns="visibleColumns"
      table-header-class="bg-grey-2"
    >
      <template v-slot:top>
        <q-input
          color="black"
          dense
          debounce="300"
          v-model="filter"
          placeholder="搜索供应商"
        >
          <template v-slot:prepend>
            <q-icon name="search" />
          </template>
          <template v-if="filter" v-slot:append>
            <q-icon name="close" @click="filter = ''" class="cursor-pointer" />
          </template>
        </q-input>
        <q-space />
        <q-select
          v-model="visibleColumns"
          multiple
          outlined
          dense
          options-dense
          display-value="列选择"
          emit-value
          map-options
          :options="columns"
          option-value="name"
          options-cover
          style="min-width: 150px"
        />
      </template>
    </q-table>
  </q-page>
</template>

<script>
import { mapState, mapGetters } from "vuex";

export default {
  name: "ShowSuppliers",
  data() {
    return {
      filter: "",
      selected: [],
      pagination: { sortBy: null, descending: false, page: 1, rowsPerPage: 5 },
      columns: [
        {
          name: "name",
          label: "供应商名称",
          align: "center",
          field: row => row.name,
          format: val => `${val}`,
          sortable: true
        },
        {
          name: "contact",
          label: "联系人",
          align: "center",
          field: row => row.contact,
          format: val => `${val}`,
          sortable: true
        },
        {
          name: "address",
          label: "地址",
          align: "center",
          field: row => row.address,
          format: val => `${val}`,
          sortable: true
        },
        {
          name: "email",
          label: "邮箱",
          align: "center",
          field: row => row.email,
          format: val => `${val}`,
          sortable: true
        },
        {
          name: "phone",
          label: "电话",
          align: "center",
          field: row => row.phone,
          format: val => `${val}`,
          sortable: true
        },
        {
          name: "website",
          label: "网站",
          align: "left",
          field: row => row.website,
          format: val => `${val}`,
          sortable: true
        },
        {
          name: "comment",
          label: "备注",
          align: "left",
          field: row => row.comment,
          format: val => `${val}`,
          sortable: true
        },
        {
          name: "created_date",
          label: "创建日期",
          align: "center",
          field: row => row.created_date,
          sortable: true
        },
        {
          name: "modified_date",
          label: "修改日期",
          align: "center",
          field: row => row.modified_date,
          sortable: true
        }
      ],
      visibleColumns: [
        "name",
        "contact",
        "email",
        "phone",
        "address",
        "website",
        "comment",
        "modified_date"
      ]
    };
  },
  methods: {
    removeSuppliers() {
      if (this.selected.length === 0) {
        this.$q.notify({
          type: "warning",
          position: "top",
          icon: "warning",
          timeout: 2000,
          message: "请先选择需要删除的产品项目。"
        });
      } else {
        this.$q
          .dialog({
            title: "确认",
            message: "确认要删除当前选定的产品吗？注意该操作无法恢复！",
            cancel: true,
            persistent: true,
            focus: "cancel"
          })
          .onOk(() => {
            let ids = this.selected.map(v => v.id);
            this.$axios
              .delete("/api/products/suppliers", {
                data: {
                  id: ids
                }
              })
              .then(res => {
                this.$store.dispatch("products/fetchSuppliers");
              });
          });
      }
    }
  },
  computed: {
    ...mapState({
      loading: state => state.products.loading,
      data: state => state.products.suppliers
    })
  },
  created: function() {
    this.$store.dispatch("products/fetchSuppliers").catch(err => {
      this.$q.notify({
        type: "negative",
        position: "top",
        icon: "warning",
        message: "无法获取供应商数据，请确认网络连接是否正常。"
      });
    });
  }
};
</script>
