export default class platypus{
    constructor(){
      this.position = {x: 500, y: 250};
      var randval = (Math.random()*2)-1;
      console.log(randval);
      this.vector = {x: randval, y: 2-randval};
    }
}
//Thanks to TheShadowNinjaYT for writing this bit