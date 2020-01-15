<template>
  <div class="app-container">
    <div class="filter-container">
      <el-row class="left">
        <el-input v-model="listQuery.device_no" placeholder="服务器编号" style="width: 300px;" class="filter-item" @keyup.enter.native="handleFilter" />
        <el-button v-waves class="filter-item" type="success" icon="el-icon-search" @click="handleFilter">
            搜索
        </el-button>
        <el-button v-waves class="filter-item" type="primary" icon="el-icon-refresh" @click="handleFilter">
            重置
        </el-button>
      </el-row>
      <el-row class="right">
        <el-button class="filter-item" style="margin-left: 10px;" type="success" icon="el-icon-plus" @click="handleCreate">
            添加
        </el-button>
        <el-button class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit" @click="handleUpdate">
            修改
        </el-button>
        <el-button class="filter-item" style="margin-left: 10px;" type="danger" icon="el-icon-delete" @click="handleDelete">
            删除
        </el-button>
        <el-button v-waves :loading="downloadLoading" class="filter-item" type="primary" icon="el-icon-download" @click="handleDownload">
            导出
        </el-button>
      </el-row>
    </div>
    <br>
    
    <el-table
      :key="tableKey"
      v-loading="listLoading"
      :data="list"
      border
      fit
      label-width="auto"
      highlight-current-row
      style="width: 100%;"
      @sort-change="sortChange"
      @current-change="handleCurrentChange"
    >
      <el-table-column label="设备编号" prop="device_no" align="center" :class-name="getSortClass('id')">
        <template slot-scope="{row}">
          <span>{{ row.device_no }}</span>
        </template>
      </el-table-column>
      <el-table-column label="服务器名称" prop="server_name" align="center" :class-name="getSortClass('id')">
        <template slot-scope="{row}">
          <span>{{ row.server_name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="服务器ip" prop="server_ip" align="center" :class-name="getSortClass('id')">
        <template slot-scope="{row}">
          <span>{{ row.server_ip }}</span>
        </template>
      </el-table-column>
      <el-table-column label="安装省份" prop="province" align="center" :class-name="getSortClass('id')">
        <template slot-scope="{row}">
          <span>{{ row.province }}</span>
        </template>
      </el-table-column>
      <el-table-column label="安装城市" prop="city" align="center" :class-name="getSortClass('id')">
        <template slot-scope="{row}">
          <span>{{ row.city }}</span>
        </template>
      </el-table-column>
      <el-table-column label="安装县区" prop="county" align="center" :class-name="getSortClass('id')">
        <template slot-scope="{row}">
          <span>{{ row.county }}</span>
        </template>
      </el-table-column>
      <el-table-column label="安装公司" prop="company" align="center" :class-name="getSortClass('id')">
        <template slot-scope="{row}">
          <span>{{ row.company }}</span>
        </template>
      </el-table-column>
      <el-table-column label="服务器状态" prop="server_state" align="center" :class-name="getSortClass('id')">
        <template slot-scope="{row}">
          <span>{{ row.server_state }}</span>
        </template>
      </el-table-column>
    </el-table>

    <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.limit" @pagination="getList" />
    <!-- 添加/修改  弹出框 -->
    <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogFormVisible">
      <el-form ref="dataForm" :rules="rules" :model="temp" label-position="right" label-width="120px">
        <el-row>
          <el-col :span="12">
            <el-form-item label="设备编号" prop="device_no">
            <el-input v-model="temp.device_no" />
          </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="服务器名称" prop="server_name">
              <el-input v-model="temp.server_name" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="服务器ip" prop="server_ip">
            <el-input v-model="temp.server_ip" />
          </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="安装省份" prop="province">
              <el-input v-model="temp.province" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="安装城市" prop="city">
              <el-input v-model="temp.city" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="安装县区" prop="county">
              <el-input v-model="temp.county" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="安装公司" prop="company">
              <el-input v-model="temp.company" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="服务器状态" prop="server_state">
              <el-input v-model="temp.server_state" />
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">
          取消
        </el-button>
        <el-button type="primary" @click="dialogStatus==='create'?createData():updateData()">
          确定
        </el-button>
      </div>
    </el-dialog>

    <el-dialog :visible.sync="dialogPvVisible" title="Reading statistics">
      <el-table :data="pvData" border fit highlight-current-row style="width: 100%">
        <el-table-column prop="key" label="Channel" />
        <el-table-column prop="pv" label="Pv" />
      </el-table>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="dialogPvVisible = false">Confirm</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import { getServerList, addServer, editServer, deleteServer } from '@/api/devices/server/server'
import waves from '@/directive/waves' // waves directive
import { parseTime } from '@/utils'
import Pagination from '@/components/Pagination' // secondary package based on el-pagination

const calendarTypeOptions = [
  { key: 'CN', display_name: 'China' },
  { key: 'US', display_name: 'USA' },
  { key: 'JP', display_name: 'Japan' },
  { key: 'EU', display_name: 'Eurozone' }
]

// arr to obj, such as { CN : "China", US : "USA" }
const calendarTypeKeyValue = calendarTypeOptions.reduce((acc, cur) => {
  acc[cur.key] = cur.display_name
  return acc
}, {})

export default {
  name: 'Server',
  components: { Pagination },
  directives: { waves },
  filters: {
    statusFilter(status) {
      const statusMap = {
        published: 'success',
        draft: 'info',
        deleted: 'danger'
      }
      return statusMap[status]
    },
    typeFilter(type) {
      return calendarTypeKeyValue[type]
    }
  },
  data() {
    return {
      tableKey: 0,
      list: null,
      isAdd: true,
      total: 0,
      // 选择行
      selRow: {},
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 10,
        importance: undefined,
        title: undefined,
        type: undefined,
        sort: '+id'
      },
      importanceOptions: [1, 2, 3],
      calendarTypeOptions,
      sortOptions: [{ label: 'ID Ascending', key: '+id' }, { label: 'ID Descending', key: '-id' }],
      statusOptions: ['published', 'draft', 'deleted'],
      showReviewer: false,
      temp: {
        device_no: '',
        server_name: '',
        server_ip: '',
        province: '',
        city: '',
        county: '',
        company: '',
        server_state: ''
      },
      // 弹出框是否可见
      dialogFormVisible: false,
      // 弹出框的状态
      dialogStatus: '',
      // 弹出框的标题
      textMap: {
        update: '修改服务器信息',
        create: '添加服务器'
      },
      dialogPvVisible: false,
      pvData: [],
      rules: {
        type: [{ required: true, message: 'type is required', trigger: 'change' }],
        timestamp: [{ type: 'date', required: true, message: 'timestamp is required', trigger: 'change' }],
        title: [{ required: true, message: 'title is required', trigger: 'blur' }]
      },
      downloadLoading: false
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      this.listLoading = true
      getServerList(this.listQuery).then(response => {
        this.list = response.data.items
        this.total = response.data.total

        // Just to simulate the time of the request
        setTimeout(() => {
          this.listLoading = false
        }, 1.5 * 1000)
      })
    },
    handleFilter() {
      this.listQuery.page = 1
      this.getList()
    },
    sortChange(data) {
      const { prop, order } = data
      if (prop === 'id') {
        this.sortByDeviceNo(order)
      }
    },
    // 通过设备编号搜索
    sortByDeviceNo(order) {
      console.log(order, 'oooooooooooo');
      if (order === 'ascending') {
        this.listQuery.sort = '+id'
      } else {
        this.listQuery.sort = '-id'
      }
      this.handleFilter()
    },
    handleCurrentChange(currentRow, oldCurrentRow) {
      this.selRow = currentRow;
    },
    resetTemp() {
      this.temp = {
        device_no: '',
        server_name: '',
        server_ip: '',
        province: '',
        city: '',
        county: '',
        company: '',
        server_state: ''
      }
    },
    // 添加
    handleCreate() {
      this.resetTemp()
      this.dialogStatus = 'create'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    createData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          this.temp.id = parseInt(Math.random() * 100) + 1024 // mock a id
          this.temp.author = 'vue-element-admin'
          addServer(this.temp).then(() => {
            this.list.unshift(this.temp)
            this.dialogFormVisible = false
            this.$notify({
              title: 'Success',
              message: '添加成功',
              type: 'success',
              duration: 2000
            })
          })
        }
      })
    },
    // 选择行
    checkSel() {
      if(this.selRow && this.selRow.device_no) {
        return true;
      }
      this.$message({
        message: '请选中操作项',
        type: 'warning'
      })
      return false;
    },
    // 修改
    handleUpdate() {
      if(this.checkSel()) {
        this.isAdd = false;
        this.dataForm = this.selRow;
        console.log(this.dataForm, 'ffffffffffff');
        this.dialogStatus = 'update';
        this.dialogFormVisible = true;
      }
      // this.temp = Object.assign({}, row) // copy obj
      // this.temp.timestamp = new Date(this.temp.timestamp)
      // this.dialogStatus = 'update'
      // this.dialogFormVisible = true
      // this.$nextTick(() => {
      //   this.$refs['dataForm'].clearValidate()
      // })
    },
    updateData() {
      console.log('修改了吗？');
      this.$refs['dataForm'].validate((valid) => {
        console.log('进来了吗？');
        if (valid) {
          console.log('正在验证')
          console.log(this.temp, 'tttttttttttttttttt');
          const tempData = Object.assign({}, this.temp)
          console.log(tempData, 't111111111111111111');
          
          // tempData.timestamp = +new Date(tempData.timestamp) // change Thu Nov 30 2017 16:41:05 GMT+0800 (CST) to 1512031311464
          updateArticle(tempData).then(() => {
            console.log('进来了');
            const index = this.list.findIndex(v => v.id === this.temp.id)
            this.list.splice(index, 1, this.temp)
            this.dialogFormVisible = false
            this.$notify({
              title: 'Success',
              message: '修改成功',
              type: 'success',
              duration: 2000
            })
          })
        }
      })
    },
    handleDelete() { 
      if(this.checkSel()) {
        var id = this.selRow.unique_server_id;
        console.log(id, 'iiiiiiiiiiii');
        this.$confirm('确定要删除该记录吗?', '提示消息', {
        })
        .then(() => {
          deleteServer(id).then(response => {
            this.$message({
              message: '删除成功',
              type: 'success'
            })
            this.getList();
          })
          console.log('删除失败');
          
        })
      }
    },
    handleFetchPv(pv) {
      console.log(pv, 'ppppppppppp');
      fetchPv(pv).then(response => {
        this.pvData = response.data.pvData
        this.dialogPvVisible = true
      })
    },
    handleDownload() {
      this.downloadLoading = true
      import('@/vendor/Export2Excel').then(excel => {
        const tHeader = ['timestamp', 'title', 'type', 'importance', 'status']
        const filterVal = ['timestamp', 'title', 'type', 'importance', 'status']
        const data = this.formatJson(filterVal)
        excel.export_json_to_excel({
          header: tHeader,
          data,
          filename: 'table-list'
        })
        this.downloadLoading = false
      })
    },
    formatJson(filterVal) {
      return this.list.map(v => filterVal.map(j => {
        if (j === 'timestamp') {
          return parseTime(v[j])
        } else {
          return v[j]
        }
      }))
    },
    getSortClass: function(key) {
      const sort = this.listQuery.sort
      return sort === `+${key}` ? 'ascending' : 'descending'
    }
  }
}
</script>
<style lang="scss" scoped>
    .filter-container {
      display: flex;
      justify-content: space-between;
    }
</style>
