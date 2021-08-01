<template>
  <q-page class="q-ma-xs q-mr-md q-pa-xs q-gutter-md">
    <q-btn-group rounded push>
      <q-btn
        label="新建"
        icon="add_circle_outline"
        @click="$router.push('/customers/new')"
        color="primary"
      />
      <q-btn
        label="修改"
        :disable="selected.length !== 1"
        icon="edit"
        @click="
          $router.push({
            path: '/customers/edit',
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
        @click="removecustomers"
        color="primary"
      />
    </q-btn-group>
    <q-btn-group rounded>
      <q-btn
        label="导出"
        icon="file_download"
        @click="$router.push('/customers/download')"
        color="primary"
      />
      <q-btn
        label="导入"
        icon="file_upload"
        @click="$router.push('/customers/upload')"
        color="primary"
      />
    </q-btn-group>

    <div>
      <q-tabs
        v-model="customersFilter"
        align="left"
        inline-label
        class="bg-grey-4 text-primary shadow-2"
        :breakpoint="300"
      >
        <q-tab name="all" label="所有客户" icon="business_center" />
        <q-tab name="valid" label="有效客户" icon="visibility" />
        <q-tab name="unvalid" label="无效客户" icon="visibility_off" />
      </q-tabs>
      <q-table
        ref="customersTable"
        :loading="loading"
        :data="data"
        :columns="columns"
        row-key="id"
        selection="multiple"
        :selected.sync="selected"
        :pagination.sync="pagination"
        :filter="filter"
        :visible-columns="visibleColumns"
        @row-dblclick="showCustomerCard"
        table-header-class="bg-grey-2"
      >
        <template v-slot:top>
          <q-input
            color="black"
            dense
            debounce="300"
            v-model="filter"
            placeholder="搜索客户"
          >
            <template v-slot:prepend>
              <q-icon name="search" />
            </template>
            <template v-if="filter" v-slot:append>
              <q-icon
                name="close"
                @click="filter = ''"
                class="cursor-pointer"
              />
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
    </div>

    <q-dialog v-model="isShowCard">
      <q-card class="my-card">
        <q-card-section>
          <div class="row no-wrap items-center">
            <div class="col">
              <q-badge
                class="text-subtitle2"
                color="accent"
                align="middle"
                :label="currentCustomer.company"
              />
            </div>
            <div
              class="col-auto text-subtitle1 q-pt-none row no-wrap items-center"
            >
              {{ currentCustomer.importance>0 ? '⭐'.repeat(currentCustomer.importance) : '🌚'}}
            </div>
          </div>
        </q-card-section>
        <q-card-section>
          <div class="text-wrapper">{{ currentCustomer.comment }}</div>
        </q-card-section>

        <q-separator />

        <q-card-actions align="right">
          <q-btn v-close-popup flat color="primary" label="关闭" />
        </q-card-actions>
      </q-card>
    </q-dialog>
  </q-page>
</template>

<script>
import { mapState, mapGetters } from "vuex";

export default {
  data() {
    return {
      customersFilter: "valid",
      filter: "",
      selected: [],
      pagination: { sortBy: null, descending: false, page: 1, rowsPerPage: 5 },
      columns: [
        {
          name: "company",
          label: "公司名",
          align: "left",
          field: row => row.company,
          format: val => `${val}`,
          sortable: true
        },
        {
          name: "importance",
          label: "客户评级",
          align: "left",
          field: row => row.importance,
          format: val => val>0 ? '⭐'.repeat(val) : '🌚',
          sortable: true
        },
        {
          name: "country",
          label: "国家",
          align: "center",
          field: row => row.country,
          format: val => val || "(无)",
          sortable: true
        },
        {
          name: "address",
          label: "公司地址",
          align: "left",
          field: row => row.address,
          format: val => val || "(无)",
          sortable: true
        },
        {
          name: "website",
          label: "公司网站",
          align: "left",
          field: row => row.website,
          format: val => val || "(无)",
          sortable: true
        },
        {
          name: "comment",
          label: "备注信息",
          align: "left",
          style: "width: 50px",
          field: row => row.comment,
          format: val => val || "(无)",
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
        },
        {
          name: "valid",
          label: "有效客户",
          align: "center",
          field: row => row.valid,
          format: val => val==0 ? "❌" : (val==1 ? "✅" : "❓"),
          sortable: true
        }
      ],
      visibleColumns: [
        "company",
        "importance",
        "country",
        "address",
        "website",
        "comment",
        "created_date",
        "modified_date",
        "valid"
      ],
      currentCustomer: {},
      isShowCard: false
    };
  },
  watch: {
    customersFilter: function(val, oldVal) {
      this.$store.commit("customers/setCustomersFilter", val);
      this.selected = [];
    }
  },
  methods: {
    showCustomerCard(evt, row, index) {
      this.currentCustomer = row;
      this.isShowCard = true;
    },
    removeCustomers() {
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
              .delete("/api/products", {
                data: {
                  id: ids
                }
              })
              .then(res => {
                this.$store.dispatch("products/fetchProducts");
              });
          });
      }
    }
  },
  computed: {
    ...mapState({
      loading: state => state.customers.loading,
      currentFilter: state => state.customers.validFilter
    }),
    ...mapGetters({
      data: "customers/filteredCustomers"
    })
  },
  created: function() {
    this.customersFilter=this.currentFilter
    this.$store.dispatch("customers/fetchCustomers").catch(err => {
      this.$q.notify({
        type: "negative",
        position: "top",
        icon: "warning",
        message: "无法获取客户数据，请确认网络连接是否正常。"
      });
    });
  }
};
</script>

<style>
.my-card {
  max-width: 100%;
  min-width: 400px;
}
.text-wrapper {
  white-space: pre-wrap;
}
</style>
