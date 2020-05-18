<template>
  <div class="index">
    <s-header></s-header>
    <router-view/>
    <s-footer></s-footer>
  </div>
</template>
<script>
import sHeader from '@/components/header/header.vue';
import sFooter from '@/components/footer/footer.vue';
export default {
  name: '',
  components: {
    sHeader,
    sFooter
  },
  data() {
    return {}
  }
}
</script>
<style scoped lang="scss">
  .bigPic{
    padding-top: 100px;
    text-align: center;
    margin-bottom: 15px;
    img{
      width: 100%;
      height: 400px;
    }
    .desc{
      margin: 0 auto;
      width: 50%;
      p{
        color: #111;
      }
      .shop{
        display: inline-block;
        margin: 5px 0;
        padding: 0 20px;
        height: 40px;
        line-height: 40px;
        background-color: #000;
        color: #fff;
        font-size: .8em;
        letter-spacing: -0.1em;
      }
    }
  }
</style>
