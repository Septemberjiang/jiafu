<template>
  <div class='basic'>
    <el-row>
      <el-col :span='24'>
        <el-card>
          <div slot="header">
            <!-- 面包屑 -->
            <el-breadcrumb separator="/" style="margin-bottom: 10px">
              <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
              <el-breadcrumb-item>摄像头列表</el-breadcrumb-item>
            </el-breadcrumb>
            <el-button type="primary" class="add_button" size="mini" @click="add_server()">新增设备</el-button>
          </div>
          <div class="table-wrapper">
              <!-- v-loading="loading" -->
            <el-table
              element-loading-text="加载数据中"
              :data='table_data'
              border
              :row-class-name="addRowClass"
               fit="true">
              <el-table-column label="设备编号" prop="device_no" align="center" width="120"></el-table-column>
              <el-table-column label="摄像头名称" prop="camera_name" align="center" width="120"></el-table-column>
              <el-table-column label="摄像头IP" prop="camera_ip" align="center" width="120"></el-table-column>
              <el-table-column label="安装位置" prop="camera_position" align="center" width="120"></el-table-column>
              <el-table-column label="rtsp地址" prop="rtsp_address" align="center" width="120"></el-table-column>
              <el-table-column label="识别阈值" prop="distinguish_wide" align="center" width="120"></el-table-column>
              <el-table-column label="检测间隔" prop="check_space" align="center" width="120"></el-table-column>
              <el-table-column label="场景识别度" prop="scene_at_degree" align="center" width="120"></el-table-column>
              <el-table-column label="移动检测阈值" prop="move_check_wide" align="center" width="120"></el-table-column>
              <el-table-column label="设备是否启用" prop="equipment_state" align="center" width="120"></el-table-column>
              
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
  import {formatDate} from 'src/utils/utils';
  // import score from 'src/components/Score/index';

  const POSITIVE = 0;
  const NEGATIVE = 1;
  export default {
    created () {
      // this.getTableData();
    },
    data () {
      return {
        table_data: [],
        loading: true,
        // 默认分页条数
        pagesize: 10,
        currentpage: 1,
        total: 0,
        show_server: ""
      }
    },
    methods: {
      // 添加
      add_server() {
         this.$router.push({
          path: '/add_camera'
        })
        console.log('00000000000');
      },
      // 查看
      view(index, row) {
        console.log(row, '11111111111111111111111111')
          // 摄像头详细信息
          this.show_server = `
            设备编号：${ row.device_no }
            摄像头名称：${ row.camera_name }
            摄像头IP: ${ row.camera_ip }
            安装位置： ${ row.camera_position }
            rtsp地址： ${ row.rtsp_address }
            识别阈值 ${ row.distinguish_wide }
            检测间隔 ${ row.check_space }
            场景相识度 ${ row.scene_at_degree }
            移动检测阈值 ${ row.move_check_wide }
            设备是否启用： ${ row.equipment_state }
          `;
          this.$alert(this.show_server, '设备详细信息', {
          confirmButtonText: '确定',
        });
      },
      // 编辑
      edit(index, row) {
        console.log(index, '22222222222222222222');
        this.$router.push({
          path: '/edit_camera',
           query: {
            id: index,
            data: row
          }
        })
        .then(res => {})
        .catch(err => {})
      },
      // 删除
      del(index, row) {
        console.log(index, 'index 11111111111111', row, 'row111111111');
        // this.tableData.splice(index, 1);
        /* 调取删除接口， 传入unique_server_id   进行确定 */
        this.axios({
          // url: `getTableData?per_page=${this.pagesize}&cur_page=${this.currentpage}`,
          // method: "get",
        //  url: "http://192.168.0.188:5000/api/device/server/operate/" + row.unique_server_id,
        //  method: "delete",
        //  data: {
        //     // id: index
        //   }
        })
        .then(res => {
          console.log(res, 'res  delete');
        })
        .catch(err => {
          console.log(err, 'errr   delete');
        })
        // console.log('333333333333333333');
      },
      // getTableData () {
      //   this.axios.get(`getTableData?per_page=${this.pagesize}&cur_page=${this.currentpage}`)
      //   .then(data => {
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
      show (scope) {
        console.log(scope, 'scope');
      },
      // 改变每页条数
      handleSizeChange (value) {
        this.pagesize = value;
        // this.getTableData();
      },
      // 当前页数
      handleCurrentChange (value) {
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
      url: "http://192.168.0.167:5000/api/device/camera/exhibition",
      method: "get"
    })
      .then(res => {
        console.log(res, 'rrrrrrrrrrrrrrrrrrrr');
        this.tableData = res.data.data;
        console.log(this.tableData, 'tableData');
        
        this.loading = false;
        
        // console.log(res.data, '11111111111111rrrrrrrrrrrrrrrr');
        // this.total =  this.tableData.length;
        // this.tableData = res.data.data;
        // console.log(this.tableData.length, 'this.tableData')
        // this.loading = false;
      })
      .catch(err => {
        console.log(err,'eeeeeeeeeee');
      });
    }
    // filters: {
    //   rateTypeToText (rateType) {
    //     return rateType === POSITIVE ? '满意' : '不满意';
    //   },
    //   formatDate (time) {
    //     let date = new Date(time);
    //     return formatDate(date, 'yyyy-MM-dd hh:mm:ss');
    //   }
    // },
    // components: {
    //   // score
    // }
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
