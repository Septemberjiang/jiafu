<template>
  <div class='basic'>
    <el-row>
      <el-col :span='24'>
        <el-card>
          <div slot="header">
            <!-- 面包屑 -->
            <el-breadcrumb separator="/" style="margin-bottom: 10px">
              <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
              <el-breadcrumb-item>设备列表</el-breadcrumb-item>
            </el-breadcrumb>
            <el-button type="primary" class="add_button" size="mini" @click="add_server()">新增设备</el-button>
          </div>
          <div class="table-wrapper">
              <!-- v-loading="loading" -->

            <el-table
              element-loading-text="加载数据中"
              :data='tableData'
              border
              :row-class-name="addRowClass"
              fit= 'true'
              >
              <el-table-column label="设备编号" prop="device_no" align="center" ></el-table-column>
              <el-table-column label="服务器名称" prop="server_name" align="center"></el-table-column>
              <el-table-column label="服务器IP" prop="server_ip" align="center"></el-table-column>
              <el-table-column label="安装省份" prop="province" align="center"></el-table-column>
              <el-table-column label="安装地市" prop="city" align="center"></el-table-column>
              <el-table-column label="安装区县" prop="county" align="center"></el-table-column>
              <el-table-column label="安装公司" prop="company" align="center"></el-table-column>
              <el-table-column label="服务器是否开启" prop="server_state" align="center"></el-table-column>
              
              <el-table-column label="操作" align="center" header-align="center" fixed="right" width="250px">
                <template slot-scope="scope">
                  <el-button type="primary" size="mini" @click="view(scope.$index, scope.row)">查看</el-button>
                  <el-button type="primary" size="mini" @click="edit(scope.$index, scope.row)">编辑</el-button>
                  <el-button type="danger" size="mini" @click="del(scope.$index, scope.row)">删除</el-button>
                </template>
                
              </el-table-column>
             
            </el-table>
            <!-- 分页 pagination -->
            <el-pagination
              style="margin-top: 16px; text-align:right;"
              layout="total, sizes, prev, pager, next, jumper"
              :page-sizes="[5, 10, 15, 20]"
              :total="total"
              @size-change="handleSizeChange"
              @current-change="handleCurrentChange">
            </el-pagination>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>
<script>
  // import {formatDate} from 'src/utils/utils';

  const POSITIVE = 0;
  const NEGATIVE = 1;
  export default {
    created () {
      // this.getTableData();
    },
    data () {
      return {
        tableData: [],
        loading: true,
        // 默认分页条数
        pagesize: 10,
        // 默认显示第一页
        currentpage: 1,
        // 总页数
        total: 0,
        show_server: ""
      }
    },
    inject: ["reload"],

    methods: {
      // 添加
      add_server() {
        this.$router.push({
          path: '/add_server'
        })
        console.log('00000000000');
      },
      // 查看
      view(index, row) {
        console.log(row, '11111111111111111111111111')
          // 该设备详细信息
          this.show_server = `
            设备编号：${ row.device_no }
            服务器名称：${ row.server_name }
            服务器IP: ${ row.server_ip }
            安装省份： ${ row.province }
            安装市县： ${ row.city }
            安装区县： ${ row.county }
            服务器是否开启： ${ row.server_state }
          `;
          this.$alert(this.show_server, '设备详细信息', {
          confirmButtonText: '确定',
        });
      },
      // 编辑
      edit(index, row) {
        // console.log(index, '22222222222222222222');
        // console.log(row.unique_server_id, 'iiiiiiiiiiiiii');
        
        this.$router.push({
          path: '/edit_server',
           query: {
             unique_server_id: row.unique_server_id,
             data: row
          }
        })
        .then(res => {})
        .catch(err => {})
      },
      // 删除
      del(index, row) {
        console.log(row.unique_server_id, 'iiiiiiiiiiiiiiiiiii');
        // this.tableData.splice(index, 1);
        this.$axios({
          url: "http://192.168.0.167:5000/api/device/server/operate/" + row.unique_server_id,
          method: "delete",
        })
        .then(res => {
          console.log(res, 'rrrrrrrrrrr');
          console.log(this, 'ttttttttttttt');
          this.reload();
          // this.loading = false;
          // window.location.reload();
        })
        .catch(err => {
          console.log(err, 'eeeeeeeeeeeeeeee');
        })
      },
      // getTableData () {
      //   this.axios({
      //     url: `getTableData?per_page=${this.pagesize}&cur_page=${this.currentpage}`,
      //     method: 'get'
      //   })
      //   .then(data => {
        // console.log(data, 'data');
        
      //     if (data.errno === 0) {
      //       this.tableData = data.data.table;
      //       this.total = data.data.total;
      //       this.loading = false;
      //     } else {
      //       console.log(data.msg);
      //     }
      //   })
      //   .catch(error => {
      //     console.log(error);
      //   });
      // },
      // *****
      show (scope) {
        console.log(scope, 'scope');
      },
      // // 每页条数
      handleSizeChange (value) {
        console.log(value,'vvvvvvvvvvvvvvvvvvv');
        
        this.pagesize = value;
        // this.getTableData();
      },
      // 当前页码
      handleCurrentChange (value) {
        console.log(value, 'aaaaaaaaaaaaaa');
        
        this.currentpage = value;
        // this.getTableData();
      },
      addRowClass ({row, rowIndex}) {
        if (row.rateType === NEGATIVE) {
          return 'warning-row';
        }
      }
    },
    // 挂载
    mounted() {
    this.$axios({
      url: "http://192.168.0.167:5000/api/device/server",
      method: "get"
    })
      .then(res => {
        console.log(res.data, '11111111111111rrrrrrrrrrrrrrrr');
        this.total =  this.tableData.length;
        this.tableData = res.data.data;
        console.log(this.tableData.length, 'this.tableData')
        this.loading = false;
      })
      .catch(err => {
        console.log(err,'eeeeeeeeeee');
      });
  },
    // filters: {
    //   rateTypeToText (rateType) {
    //     return rateType === POSITIVE ? '满意' : '不满意';
    //   },
    //   formatDate (time) {
    //     let date = new Date(time);
    //     return formatDate(date, 'yyyy-MM-dd hh:mm:ss');
    //   }
    // },
    components: {
      // score
    }
  };
</script>
<style lang='scss'>
  .basic {
    .el-table {
      .warning-row {
        background-color: oldlace;
      }
    }

    .recommend-tag {
      display: inline-block;
      margin: 4px 0;
      margin-right: 4px;

      &:last-child {
        margin-right: 0;
      }
    }
  }
</style>
