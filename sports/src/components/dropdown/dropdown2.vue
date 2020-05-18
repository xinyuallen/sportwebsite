<template>
  <div class="dropdown">
    <a
    href="javascript:;"
    v-for="(item, index) in subCategoryList"
    :key="index"
    @click="toCategory(item.subCateName)"
    >
      <img :src="`${baseUrl + item.thumbnail_img}`" alt="">
      <span>{{item.subCateName}}</span>
    </a>
  </div>
</template>
<script>
export default {
  name: 'Dropdown2',
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
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
    width: 1200px;
    left: calc(50% - 600px);
    padding: 4px;
    padding-right: 0;
    a{
      width: calc((100% - 20px)/5);
      margin-right: 4px;
      margin-bottom: 4px;
      overflow: hidden;
      position: relative;
      img{
        width: 100%;
        height: 100%;
        transition: transform 0.3s ease-in-out;
        &:hover{
          transform: scale(1.1, 1.1);
        }
      }
      span{
        position: absolute;
        font-weight: bold;
        font-size: 16px;
        width: 100%;
        text-align: center;
        line-height: normal;
        bottom: 20px;
        left: 50%;
        transform: translate(-50%, -50%);
        text-transform:uppercase;
      }
    }
  }
</style>
