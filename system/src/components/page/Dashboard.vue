
<template>
  <div class="container">
    <div class="chart" ><chart :option="option" :auto-resize="false" @click="changeConcept"></chart></div>
    
    <div>
      <el-row :gutter="20">
        <el-col :span="24">
          <el-table
            v-if="loadcomplete"
            :data="tableData.slice(0, pageSize)"
            height="tableHeight"
            style="width: 100%"
          >
            <el-table-column
              prop="title"
              label="相关文章列表"
              width="400"
              :show-overflow-tooltip="true"
            >
              <template slot-scope="scope">
                <el-button type="text" @click="openDialog(scope.row)">
                  {{ scope.row.title }}
                </el-button>
              </template>
            </el-table-column>
            <el-table-column prop="summary" label="概览" show-overflow-tooltip>
            </el-table-column>
          </el-table>
        </el-col>
      </el-row>
    </div>
    <div class="block">
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page.sync="currentPage"
        :page-size="pageSize"
        layout="prev, pager, next, jumper"
        :total="totalNum"
      >
      </el-pagination>
    </div>
  </div>
</template>



<script>
import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { PieChart } from "echarts/charts";
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
} from "echarts/components";
import VChart, { THEME_KEY } from "vue-echarts";

use([
  CanvasRenderer,
  PieChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent,
]);
export default {
  components: {
    VChart,
  },
  provide: {
    [THEME_KEY]: "light",
  },
  data() {
    return {
      option: {
        title: {
          text: "Concept Map",
          left: "center",
        },
        tooltip: {
          trigger: "item",
        },
        series: [
          {
            name: "Concept Map",
            type: "graph",
            layout:'force',
            edgeSymbol:['','arrow'],
            label:{
              show:true
            },
            force:{
              repulsion:1000
            },
            draggable:true,
            data: [
              {
                name: "数据结构",
                fixed : false
              },
              {
                name: "算法",
                fixed : false
              },
              {
                name: "排序",
                fixed : false
              },
            ],
            links: [
              {
                source: "数据结构",
                target: "算法",
                value:0.5,
              },
              {
                source: "算法",
                target: "排序",
                value:0.7
              },
            ],
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: "rgba(0, 0, 0, 0.5)",
              },
            },
          },
        ],
      },
      inlinks : [],
      outlinks : [],
      tableData: [],
      tableHeight: window.innerHeight - 100,
      currentPage: 1,
      pageSize: 10,
      totalNum: 100,
      concept:'',
      k: "0",
      m: "0",
      way: "origin",
      loadcomplete: false,
    };
  },
  methods: {
    ///分页    初始页currentPage、初始每页数据数pagesize和数据testpage
    handleSizeChange(val) {
      console.log(`每页 ${val} 条`);
      this.pageSize = val; //动态改变
    },
    changeConcept(params){
      if( params.dataType=='node'){
      console.log(params.name);
        this.$router.push({
        name: "conceptpage",
        params: { map: decodeURI(window.location.href.split('/').reverse()[1]), concept: params.name },
      });
      }
      
    },
    changetable(page) {
      var begin = (page - 1) * this.pageSize;
      //加载val页信息
      let _this = this;
      
      this.$http
        .request({
          url : _this.$url + "/getArticleList?concept=" + decodeURI(window.location.href.split('/').reverse()[0]) + "&startNum=" + begin,
          method : "get",
        })
        .then(function (response) {
          (_this.tableData = response.data.articles),
            (_this.loadcomplete = true);
            //console.log(begin),
            //console.log(response.data.papers),
            console.log(_this.tableData);
        })
        .catch(function (error) {
          console.log(error);
        });

      //获取论文列表个数
      /*this.$http
        .request({
          url:
            _this.$url +
            "/getPaperNum?method=" +
            _this.way +
            "&query=" +
            _this.k,
          method: "get",
        })
        .then(function (response) {
          //console.log(response),
          (_this.totalNum = response.data.num),
            console.log("获取论文列表个数"),
            console.log(_this.totalNum);
        })
        .catch(function (error) {
          console.log(error);
        });*/

      /*_this.loadcomplete = true;
      _this.tableData = [
        {
          title:'第一篇文章',
          summary:'abcdefg',
          id:1
        },
        {
          title:'第二篇文章',
          summary:'1145141919810',
          id:2
        }
      ];*/
      _this.totalNum = 100;
    },
    handleCurrentChange(val) {
      console.log(`当前页: ${val}`);
      this.currentPage = val;
      //console.log(this.tabelData);
    },
    openDialog(paper) {
      //console.log("get!");
      //this.$router.push({path: '/readpage' });
      //console.log(`dash: ${paper.pdfLink}`);
      this.$router.push({
        name: "readpage",
        params: { concept:decodeURI(window.location.href.split('/').reverse()[0]),id: paper.id },
      });
    },
    getData() {
      let _this = this;
      this.$http
        .request({
          url : _this.$url + "/getRelatedConcept?concept=" +decodeURI(window.location.href.split('/').reverse()[0])+ "&field=" +decodeURI(window.location.href.split('/').reverse()[1]),
          method : "get",
        })
        .then(function (response) {
          (_this.inlinks = response.data.inlinks),
            (_this.outlinks = response.data.outlinks),
            (_this.concept = response.data.name)
            //console.log(begin),
            //console.log(response.data.papers),
            console.log(_this.outlinks);
            var inlinks = _this.inlinks;
            var outlinks = _this.outlinks;
            var concept=  _this.concept;
            var nodes = [];
            var edges = [];

            nodes.push({
              name:concept,
              fixed:false
            });
            for(var i = 0;i<inlinks.length;i++){
              nodes.push({
                name:inlinks[i].name,
                fixed:false,
                draggable:true
              });
              edges.push({
                source: inlinks[i].name,
                target: concept,
                value:inlinks[i].value,
              });
            }
            for(var i = 0;i<outlinks.length;i++){
              nodes.push({
                name:outlinks[i].name,
                fixed:false,
                draggable:true
              });
              edges.push({
                source: concept,
                target: outlinks[i].name,
                value: outlinks[i].value,
              });
            }
            console.log(nodes);
            _this.option.series[0].data = nodes;
            _this.option.series[0].links = edges;
        })
        .catch(function (error) {
          console.log(error);
        });
      //加载列表首页信息
      this.changetable(1);
    },
  },
  watch: {
    $route(to, from) {
      this.tabelData = new Array(this.pageSize);
      this.getData(this.$route.query);
    },
    currentPage(newv, oldv) {
      console.log("in watch");
      console.log(newv);
      this.changetable(newv);
    },
  },
  created() {
    this.tabelData = new Array(this.pageSize);
    this.getData();
  },
};
</script>
<style>
.el-tooltip__popper {
  max-width: 100%;
}
</style>
<style scoped>
.all {
  display: flex;
}
.el-row {
  /*
  top:30px;
  bottom: 70px;
  right:0px;
  width:100%;
  position: absolute;
  z-index:1;
  */
  top: 4%;
  bottom: 4%;
  left: 50%;
  right: 0px;
  width: 50%;
  position: absolute;
  overflow-y: scroll;
  z-index: 1;
}
.el-row ::-webkit-scrollbar {
  width: 0;
}
.el-row > ul {
  height: 100%;
}
.block {
  /*
  bottom:0px;
  left: 800px;
  position:fixed;
  z-index:1;
  */
  bottom: 0px;
  left: 60%;
  position: fixed;
  z-index: 1;
}

.chart {
  left: 0%;
  top: 0%;
  width: 50%;
  height:100%;
}
.container {
  width: 100%;
  height: 100%;
}
.test {
  height: 500px;
}
</style>