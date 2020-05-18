<template>
  <div class="language">
    <div class="language-header">
      <a href="/"><img src="../../assets/logo.jpg" alt=""></a>
      <h2>SELECT YOUR LOCATION</h2>
    </div>
    <div class="state">
      <div
      class="state-child"
      v-for="(item, index) in stateArr"
      :key="index"
      @click="changeState(index)"
      >
        <span :class="stateStatus[index] ? 'click' : ''"></span>
        <div class="state-name">
          {{item}}
        </div>
      </div>
    </div>
    <ul class="country">
      <li v-for="(item, index) in countryArr" :key="index">
        <span class="img"></span>
        <span class="countryName">{{item.countryName}}</span>
      </li>
    </ul>
  </div>
</template>
<script>
export default {
  name: '',
  data() {
    return {
      stateStatus:[false,false,false,false,false,false],
      stateArr: ['NORTH AMERICA', 'SOUTH AMERICA', 'EUROPE', 'ASIA PACIFIC', 'MIDDLE EAST', 'AFRICA'],
      countryArrAll:[[
        {imgUrl: '', countryName: 'UNITED STATES'},
        {imgUrl: '', countryName: 'UNITED'},
        {imgUrl: '', countryName: 'UNITED STATES'},
        {imgUrl: '', countryName: 'UNITED STATES'},
        {imgUrl: '', countryName: 'UNITED STATES'},
        {imgUrl: '', countryName: 'UNITED STATES'}
      ],[
        {imgUrl: '', countryName: 'fafaf STATES'},
        {imgUrl: '', countryName: 'qfawwUfafaTED'},
      ],[
        {imgUrl: '', countryName: 'wang STATES'},
        {imgUrl: '', countryName: 'qfawwUafaTED'},
      ],[
        {imgUrl: '', countryName: 'zhong STATES'},
        {imgUrl: '', countryName: 'qfawfaTED'},
      ],[
        {imgUrl: '', countryName: 'duo STATES'},
        {imgUrl: '', countryName: 'dawdawd'},
      ],[
        {imgUrl: '', countryName: 'fafaf STATES'},
        {imgUrl: '', countryName: 'adadawd'},
      ]],
      countryArr:[]
    }
  },
  methods:{
    changeState(index){
      this.stateStatus = [false,false,false,false,false,false];
      this.stateStatus.splice(index, 1, true);
      /*显示州下的国家*/
      /*this.countryArr = this.countryArrAll[index];*/
    }
  }
}
</script>
<style scoped lang="scss">
  .language{
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    position: relative;
    .language-header{
      text-align: center;
      margin-bottom: 20px;
      img{
        width: 100px;
        height: 40px;
      }
      h2{
        font-size: 30px;
        text-transform: uppercase;
        margin-top: 10px;
      }
    }
    .state{
      .state-child{
        display: inline-block;
        margin: 0 10px;
        span{
          display: block;
          width: 108px;
          height: 108px;
          background: url('../../assets/country/state.png') no-repeat;
          border: 2px solid #e5e5e5;
          cursor: pointer;
        }
        .click{
          border-color: #000;
        }
        /* through包括6，to不包括 */
        @for $i from 1 through 6{
          &:nth-child(#{$i}){
            span{
              background-position: (-108px * (6 - $i)) 0;
            }
          }
        }
        .state-name{
          font-size: 12px;
          font-weight: 800;
          text-align: center;
          width: 108px;
          margin-top: 10px;
        }
      }
    }
    .country{
      width: 720px;
      position: absolute;
      top: 70%;
      li{
        display: inline-block;
        width: 20%;
        text-align: center;
        margin-bottom: 20px;
      }
      .img{
        display: inline-block;
        width: 14px;
        height: 10px;
        background: url('../../assets/country/countries.png') no-repeat;
      }
      .countryName{
        font-size: 13px;
        text-transform: uppercase;
        font-weight: 500;
        &:hover{
          text-decoration: underline;
          cursor: pointer;
        }
      }
    }
  }
</style>
