<template>
  <div class="dropdown">
    <div class="child" v-for="(item, index) in subCategoryList" :key="index">
      <span class="img">
        <img :src="`${baseUrl + item.blend_avatar}`" alt="">
      </span>
      <div class="right">
        <div class="title"><a href="javascript:;" @click="toCategory(item.subCateName)">{{item.subCateName}}</a></div>
        <div class="desc multiLine-ellipse-5">{{item.blend_desc}}</div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'Dropdown3',
  props:['subCategoryList'],
  data() {
    return {
      baseUrl: 'http://202.195.167.248/media/'
    }
  },
  methods:{
    toCategory(categoryName){
      this.$router.push({name:'category', params:{categoryName}});
    }
  }
}
</script>
<style scoped lang="scss">
  .dropdown{
    position: absolute;
    top: 68px;
    background-color: #fff;
    width: 1000px;
    left: calc(50% - 500px);
    padding: 4px;
    padding-right: 0;
    cursor: auto;
    text-align: center;
    .child{
      margin-right: 4px;
      width: calc((100% - 14px)/2);
      display: inline-block;
      .img{
        display: inline-block;
        width: 130px;
        height: 130px;
        float: left;
        overflow: hidden;
        border-radius: 50%;
        img{
          width: 100%;
          height: 100%;
          border-radius: 50%;
          transition: transform 0.3s ease-in-out;
          &:hover{
            transform: scale(1.1, 1.1);
          }
        }
      }
      .right{
        float: right;
        line-height: normal;
        width: calc(100% - 134px);
        height: 130px;
        .title{
          font-size: 14px;
          text-align: left;
          padding-left: 20px;
          margin: 10px 0 5px;
          text-transform:uppercase;
          a{
            &:hover{
              color: #43AAE0;
            }
          }
        }
        .desc{
          font-size: 13px;
          text-align: left;
          padding-left: 20px;
          color: #999;
        }
      }
    }
  }
</style>
