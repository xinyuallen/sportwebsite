<template>
  <div class="dropdown">
    <div class="item" v-for="(item, index) in subCategoryList" :key="index">
      <!-- <img :src="`${baseUrl + item.list_icon}`" alt=""> -->
      <span>
        <a href="javascript:;" @click="toCategory(item.subCateName)">{{item.subCateName}}</a>
      </span>
    </div>
  </div>
</template>
<script>
export default {
  name: 'Dropdown1',
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
    display: flex;
    flex-direction: column;
    /* justify-content: center; */
    width: 300px;
    /* left: calc(50% - 150px); */
    margin-left: -100px;
    padding: 4px;
    padding-right: 0;
    .item{
      /* width: calc((100% - 16px)/4); */
      margin-right: 4px;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      img{
        width: 30px;
        height: 30px;
        cursor: default;
        flex: 0;
      }
      span{
        flex: 1;
        margin-left: 10px;
        font-size: 14px;
        font-weight: 500;
        line-height: 30px;
        height: 100%;
        text-transform: Capitalize;
        a{
          display: inline-block;
          height: 100%;
          border-bottom: 1px solid transparent;
          text-transform:capitalize;
          &:hover{
            color: #43AAE0;
            border-color: #43AAE0;
          }
        }
      }
    }
  }
</style>
