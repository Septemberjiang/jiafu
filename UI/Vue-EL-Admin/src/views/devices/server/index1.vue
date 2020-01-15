<template>
  <div class="app-container">
    <div class="block">
      <el-row :gutter="20" class="left">
        <el-col :span="6">
          <el-input v-model="search" placeholder="请输入搜索内容"></el-input>
        </el-col>
        <el-col :span="6">
          <el-button type="success" size="mini" @click.native="search"
            >搜索</el-button
          >
          <el-button type="primary" size="mini" @click.native="reset"
            >重置</el-button
          >
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="24" class="right">
          <el-button
            type="success"
            size="mini"
            icon="el-icon-plus"
            @click.native="add"
            >添加</el-button
          >
          <el-button
            type="primary"
            size="mini"
            icon="el-icon-edit"
            @click.native="edit"
            >编辑</el-button
          >
          <el-button
            type="danger"
            size="mini"
            icon="el-icon-delete"
            @click.native="remove"
            >删除</el-button
          >
          <el-button
            type="info"
            size="mini"
            icon="el-icon-document"
            @click.native="exportXls"
            >导出</el-button
          >
        </el-col>
      </el-row>

      <el-table
        :data="list"
        v-loading="listLoading"
        element-loading-text="加载中"
        border
        fit
        highlight-current-row
        @current-change="handleCurrentChange"
      >
        <el-table-column label="设备编号">
          <template slot-scope="scope">
            {{ scope.row.device_no }}
          </template>
        </el-table-column>
        <el-table-column label="服务器名称">
          <template slot-scope="scope">
            {{ scope.row.server_name }}
          </template>
        </el-table-column>
        <el-table-column label="服务器ip">
          <template slot-scope="scope">
            {{ scope.row.server_ip }}
          </template>
        </el-table-column>
        <el-table-column label="安装省份">
          <template slot-scope="scope">
            {{ scope.row.province }}
          </template>
        </el-table-column>
        <el-table-column label="安装城市">
          <template slot-scope="scope">
            {{ scope.row.city }}
          </template>
        </el-table-column>
        <el-table-column label="安装县区">
          <template slot-scope="scope">
            {{ scope.row.county }}
          </template>
        </el-table-column>
        <el-table-column label="安装公司">
          <template slot-scope="scope">
            {{ scope.row.company }}
          </template>
        </el-table-column>
        <el-table-column label="服务器状态">
          <template slot-scope="scope">
            {{ scope.row.server_state }}
          </template>
        </el-table-column>
      </el-table>

      <!-- 分页
      <el-pagination
        background
        layout="total, sizes, prev, pager, next, jumper"
        :page-sizes="[10, 20, 50, 100, 500]"
        :page-size="listQuery.limit"
        :total="total"
        @size-change="changeSize"
        @current-change="fetchPage"
        @prev-click="fetchPrev"
        @next-click="fetchNext"
      >
      </el-pagination>

      <el-dialog :title="formTitle" :visible.sync="formVisible" width="70%">
        <el-form ref="form" :model="form" :rules="rules" label-width="120px">
          <el-row>
            <el-col :span="12">
              <el-form-item label="设备编号" prop="device_no">
                <el-input v-model="form.device_no" minlength="1"></el-input>
              </el-form-item>
            </el-col>
            <el-col :span="12">
              <el-form-item label="服务器名称" prop="server_name">
                <el-input v-model="form.server_name" minlength="1"></el-input>
              </el-form-item>
            </el-col>
            <el-col :span="12">
              <el-form-item label="服务器IP" prop="server_name">
                <el-input v-model="form.server_ip" minlength="1"></el-input>
              </el-form-item>
            </el-col>
            <el-col :span="12">
              <el-form-item label="安装省份" prop="province">
                <el-input v-model="form.province" minlength="1"></el-input>
              </el-form-item>
            </el-col>
            <el-col :span="12">
              <el-form-item label="安装城市" prop="city">
                <el-input v-model="form.city" minlength="1"></el-input>
              </el-form-item>
            </el-col>
            <el-col :span="12">
              <el-form-item label="安装县区" prop="county">
                <el-input v-model="form.county" minlength="1"></el-input>
              </el-form-item>
            </el-col>
            <el-col :span="12">
              <el-form-item label="安装公司" prop="company">
                <el-input v-model="form.company" minlength="1"></el-input>
              </el-form-item>
            </el-col>
            <el-col :span="12">
              <el-form-item label="服务器状态" prop="server_state">
                <el-input v-model="form.server_state" minlength="1"></el-input>
              </el-form-item>
            </el-col>
          </el-row>
          <el-form-item>
            <el-button type="primary" @click="save">{{
              保存
            }}</el-button>
            <el-button @click.native="formVisible = false">{{
              取消
            }}</el-button>
          </el-form-item>
        </el-form>
      </el-dialog> -->
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      total: 0,
      list: null,
      listLoading: true
    };
  },
  methods: {
    search() {
      console.log("search")
    },
    reset() {
      console.log("reset")
    },
    add() {
      console.log("add")
    },
    edit() {
      console.log("edit")
    },
    remove() {
      console.log("remove")
    },
    exportXls() {
      console.log("exportXls")
    }
    // handleCurrentChange() {
    //   console.log("handleCurrentChange")
    // },
    // changeSize() {
    //   console.log('changeSize')
    // },
    // fetchPage() {
    //   console.log('fetchPage')
    // },
    // fetchPrev() {
    //   console.log("fetchPrev")
    // },
    // fetchNext() {
    //   console.log("fetchNext")
    // }
  }
}
</script>
<style rel="stylesheet/scss" lang="scss" scoped>
// @import "../../../styles/common.scss";
.block {
  padding: 10px 0px;
}
.el-form-item {
  margin-bottom: 20px;
}
.flash-table-expand {
  font-size: 0;
}

.flash-table-expand .el-form-item {
  margin-right: 0;
  margin-bottom: 0;
  width: 50%;
}
.user {
  padding: 10px;
}
.user > strong {
  color: #777;
  font-size: 15px;
  font-weight: 400;
}

.user > small {
  color: #9e9e9e;
}

.user-content {
  box-shadow: 2px 2px 4px #edecec;
  min-height: 500px;
}

.user-content > .profile {
  background: #edecec;
  padding: 10px;
  height: 500px;
  width: 220px;
}
.user-content > .profile > img {
  width: 100%;
}
</style>
