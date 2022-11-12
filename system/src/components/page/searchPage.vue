
<template>
<div class = 'content'>
    <h1 class = 'title'>{{title}}</h1>
    <p class = 'url'>来源网站：{{url}}</p>
    <p v-for="m in message" class = 'textt'>{{m}}</p>
    
</div>
</template>


<script>
export default {
 data() {	
	return {
        message:[],
    };
    },
    created() {
        let _this = this;
        this.$http
        .request({
          url : _this.$url + "/getArticle?concept=" +decodeURI(window.location.href.split('/').reverse()[1])+ "&articleID=" +decodeURI(window.location.href.split('/').reverse()[0]),
          method : "get",
        })
        .then(function (response) {
          (_this.message = response.data.text.split('xzh')),
            (_this.title = response.data.title),
            (_this.url = response.data.url)
            //console.log(begin),
            //console.log(response.data.papers),
        })
        .catch(function (error) {
          console.log(error);
        });
      //加载列表首页信息
    },

}
</script>
<style>
    .el-tooltip__popper{max-width:40%}
</style>
<style scoped>
.content {
	/*
  top:30px;
  bottom: 70px;
  right:0px;
  width:100%;
  position: absolute;
  z-index:1;
  */
  top:4%;
  bottom: 4%;
  left:20%;
  right:20%;
  position: absolute;  
  overflow-y: scroll;
  z-index:1;
  word-break:break-all;
  background-color: beige;
}
.title{
  text-align: center;
}
.url{
  text-align: center;
}
.textt{
  text-indent: 30px;
}
</style>