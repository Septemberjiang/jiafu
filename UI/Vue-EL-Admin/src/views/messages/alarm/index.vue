<template>
  <div class="app-container">
    <div class="filter-container">
      <el-row class="left">
        <el-input v-model="listQuery.title" placeholder="Title" style="width: 300px;" class="filter-item" @keyup.enter.native="handleFilter" />
        <el-button v-waves class="filter-item" type="success" icon="el-icon-search" @click="handleFilter">
            搜索
        </el-button>
        <el-button v-waves class="filter-item" type="primary" icon="el-icon-refresh" @click="handleFilter">
            重置
        </el-button>
      </el-row>
      <el-row class="right">
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
    >
      <el-table-column label="报警内容" prop="alarm_content" align="center" :class-name="getSortClass('id')">
        <template slot-scope="{row}">
          <span>{{ row.alarm_content }}</span>
        </template>
      </el-table-column>
      <el-table-column label="报警时间" align="center">
        <template slot-scope="{row}">
          <span>{{ row.alarm_time | parseTime('{y}-{m}-{d} {h}:{i}') }}</span>
        </template>
      </el-table-column>
      <el-table-column label="人脸识别姓名" prop="face_recognition" align="center" :class-name="getSortClass('id')">
        <template slot-scope="{row}">
          <span>{{ row.face_recognition }}</span>
        </template>
      </el-table-column>
      <el-table-column label="base64图片" prop="img_base64" align="center" :class-name="getSortClass('id')">
        <template slot-scope="{row}">
          <span>{{ row.img_base64 }}</span>
        </template>
      </el-table-column>
      <el-table-column label="报警类型" prop="alarm_type" align="center" :class-name="getSortClass('id')">
        <template slot-scope="{row}">
          <span>{{ row.alarm_type }}</span>
        </template>
      </el-table-column>
      <el-table-column label="报警级别" prop="alarm_level" align="center" :class-name="getSortClass('id')">
        <template slot-scope="{row}">
          <span>{{ row.alarm_level }}</span>
        </template>
      </el-table-column>
      <el-table-column label="报警地址" prop="alarm_address" align="center" :class-name="getSortClass('id')">
        <template slot-scope="{row}">
          <span>{{ row.alarm_address }}</span>
        </template>
      </el-table-column>
      <el-table-column label="图片名称" prop="img_name" align="center" :class-name="getSortClass('id')">
        <template slot-scope="{row}">
          <span>{{ row.img_name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="图片备注" prop="img_remark" align="center" :class-name="getSortClass('id')">
        <template slot-scope="{row}">
          <span>{{ row.img_remark }}</span>
        </template>
      </el-table-column>
      <el-table-column label="图片地址" prop="img_url" align="center" :class-name="getSortClass('id')">
        <template slot-scope="{row}">
          <span>{{ row.img_url }}</span>
        </template>
      </el-table-column>
      <el-table-column label="视频地址" prop="video_url" align="center" :class-name="getSortClass('id')">
        <template slot-scope="{row}">
          <span>{{ row.video_url }}</span>
        </template>
      </el-table-column>
      <el-table-column label="事件关联项" prop="link_obj" align="center" :class-name="getSortClass('id')">
        <template slot-scope="{row}">
          <span>{{ row.link_obj }}</span>
        </template>
      </el-table-column>
    </el-table>

    <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.limit" @pagination="getList" />

    <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogFormVisible">
      <el-form ref="dataForm" :rules="rules" :model="temp" label-position="left" label-width="auto" style="width: 400px; margin-left:50px;">
        <el-form-item label="报警内容" prop="alarm_content">
          <el-input v-model="temp.alarm_content" />
        </el-form-item>
        <el-form-item label="报警时间" prop="alarm_time">
          <el-input v-model="temp.alarm_time" />
        </el-form-item>
        <el-form-item label="人脸识别姓名" prop="face_recognition">
          <el-input v-model="temp.face_recognition" />
        </el-form-item>
        <el-form-item label="base64图片" prop="img_base64">
          <el-input v-model="temp.img_base64" />
        </el-form-item>
        <el-form-item label="报警类型" prop="alarm_type">
          <el-input v-model="temp.alarm_type" />
        </el-form-item>
        <el-form-item label="报警级别" prop="alarm_level">
          <el-input v-model="temp.alarm_level" />
        </el-form-item>
        <el-form-item label="报警地址" prop="alarm_address">
          <el-input v-model="temp.alarm_address" />
        </el-form-item>
        <el-form-item label="图片名称" prop="img_name">
          <el-input v-model="temp.img_name" />
        </el-form-item>
        <el-form-item label="图片备注" prop="img_remark">
          <el-input v-model="temp.img_remark" />
        </el-form-item>
        <el-form-item label="图片地址" prop="img_url">
          <el-input v-model="temp.img_url" />
        </el-form-item>
        <el-form-item label="视频地址" prop="video_url">
          <el-input v-model="temp.video_url" />
        </el-form-item>
        <el-form-item label="事件关联项" prop="link_obj">
          <el-input v-model="temp.link_obj" />
        </el-form-item>
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
import { fetchList, fetchPv, createArticle, updateArticle } from '@/api/messages/alarm/alarm'
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
  name: 'MessageAlarm',
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
      total: 0,
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
        alarm_content: '',
        alarm_time: '',
        face_recognition: '',
        img_base64: '',
        alarm_type: '',
        alarm_level: '',
        alarm_address: '',
        img_name: '',
        img_remark: '',
        img_url: '',
        video_url: '',
        link_obj: ''
      },
      dialogFormVisible: false,
      dialogStatus: '',
      textMap: {
        update: 'Edit',
        create: 'Create'
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
      fetchList(this.listQuery).then(response => {
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
    handleModifyStatus(row, status) {
      this.$message({
        message: '操作Success',
        type: 'success'
      })
      row.status = status
    },
    sortChange(data) {
      const { prop, order } = data
      if (prop === 'id') {
        this.sortByID(order)
      }
    },
    sortByID(order) {
      if (order === 'ascending') {
        this.listQuery.sort = '+id'
      } else {
        this.listQuery.sort = '-id'
      }
      this.handleFilter()
    },
    resetTemp() {
      this.temp = {
        alarm_content: '',
        alarm_time: '',
        face_recognition: '',
        img_base64: '',
        alarm_type: '',
        alarm_level: '',
        alarm_address: '',
        img_name: '',
        img_remark: '',
        img_url: '',
        video_url: '',
        link_obj: ''
      }
    },
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
          createArticle(this.temp).then(() => {
            this.list.unshift(this.temp)
            this.dialogFormVisible = false
            this.$notify({
              title: 'Success',
              message: 'Created Successfully',
              type: 'success',
              duration: 2000
            })
          })
        }
      })
    },
    handleUpdate(row) {
      this.temp = Object.assign({}, row) // copy obj
      this.temp.timestamp = new Date(this.temp.timestamp)
      this.dialogStatus = 'update'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.temp)
          tempData.timestamp = +new Date(tempData.timestamp) // change Thu Nov 30 2017 16:41:05 GMT+0800 (CST) to 1512031311464
          updateArticle(tempData).then(() => {
            const index = this.list.findIndex(v => v.id === this.temp.id)
            this.list.splice(index, 1, this.temp)
            this.dialogFormVisible = false
            this.$notify({
              title: 'Success',
              message: 'Update Successfully',
              type: 'success',
              duration: 2000
            })
          })
        }
      })
    },
    handleDelete(row, index) {
      this.$notify({
        title: 'Success',
        message: 'Delete Successfully',
        type: 'success',
        duration: 2000
      })
      this.list.splice(index, 1)
    },
    handleFetchPv(pv) {
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
