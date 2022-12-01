gsap.registerPlugin(ScrollTrigger);

function block_anima() {
//GSAP 3 introduces advanced stagger values
var grid = [3,6], //[rows, columns]
    tl = gsap.timeline({repeat: -1, repeatDelay: 0.5});

console.log()

function animateBoxes(from, axis, ease) {
  //one stagger call does all the animation:
  tl.to(".ii-box", {
      duration: 1,
      scale: 0.1, 
      y: 100,
      yoyo: true, 
      repeat: 1, 
      ease: "power1.inOut",
      stagger: {
        amount: 1.5, 
        grid: grid, 
        axis: axis, 
        ease: ease,
        from: from
      }
    }
  );
}

//builds a grid of <div class="box"> elements, dropped into #container (unrelated to animation code)
buildGrid({grid: grid, className: "ii-box", width: 1000, gutter: 15, parent: "#ii-anim-container", onCellClick: onCellClick});

animateBoxes("random");


//---- the rest of the code below just handles all the interactivity ----

var options = document.querySelectorAll('input[name="from"], input[name="axis"], input[name="ease"]'),
    _select = function(selector) {
      return document.querySelector(selector);
    },
    axisCodeEl = _select("#axisCode"),
    axisEl = _select("#axis"),
    easeCodeEl = _select("#easeCode"),
    easeEl = _select("#ease"),
    fromEl = _select("#from"),
    fromIndexEl = _select("#fromIndex"),
    indexEl = _select("#index"),
    selections = {from: "center", axis: null, ease: "none"},
    i;

//add change listeners
for (i = 0; i < options.length; i++) {
  options[i].addEventListener("change", onOptionChange);
}

function onOptionChange(e) {
  var group = e.target.getAttribute("name"),
      value = e.target.getAttribute("value");
  if (group === "from") {
    updateFrom(value);
  } else if (group === "axis") {
    selections.axis = (value === "null") ? null : value;
    axisCode.style.display = (value === "null") ? "none" : "inline";
    axisEl.textContent = '"' + value + '"';
  } else if (group === "ease") {
    easeEl.textContent = value;
    easeCodeEl.style.display = (value === '"none"') ? "none" : "inline";
    selections.ease = value.split('"').join("");
  }
  updateAnimation();
}

function updateFrom(value) {
  var current = selections.from,
      parsedVal = value,
      newIsNumber = !isNaN(value),
      oldIsNumber = !isNaN(current);
  if (newIsNumber) {
    parsedVal = parseInt(value, 10);
  } else if (value === "end") {
    parsedVal = grid[0] * grid[1] - 1;
    newIsNumber = true;
  }
  if (current !== parsedVal) {
    selections.from = parsedVal;
    fromEl.textContent = (value === "end") ? '"end"' : newIsNumber ? value : '"' + value + '"';
    if (newIsNumber && !oldIsNumber) {
      gsap.to(".box", {duration: 0.3, backgroundColor: "#595959"});
    } else if (!newIsNumber && oldIsNumber) {
      gsap.to(".box", {duration: 0.3, backgroundColor: "#88ce02"});
    }
    if (newIsNumber) {
      if (value !== "end") {
        indexEl.checked = true;
        indexEl.setAttribute("value", parsedVal);
        fromIndexEl.textContent = parsedVal + " (index)";
      }
      gsap.fromTo("[data-index='" + parsedVal + "']", {rotation: 0}, {duration: 0.4, rotation: 360, backgroundColor: "#88ce02", ease: "power1.inOut"});
      if (oldIsNumber) {
        gsap.to("[data-index='" + current + "']", {duration: 0.3, backgroundColor: "#595959"});
      }
    }
  }
}

function onCellClick(e) {
  updateFrom(e.target.index);
  updateAnimation();
}

function updateAnimation() {
  tl.seek(0).clear();
  animateBoxes(selections.from, selections.axis, selections.ease);
}

//helper function to build a grid of <div> elements
function buildGrid(vars) {
	vars = vars || {};
	var container = document.createElement("div"),
		rows = vars.grid[0] || 5,
		cols = vars.grid[1] || 5,
		width = vars.width || 100,
		gutter = vars.gutter || 1,
    className = vars.className || "",
		w = (width - cols * gutter) / cols,
		parent = (typeof(vars.parent) === "string") ? document.querySelector(vars.parent) : vars.parent ? vars.parent : document.body,
		css = "display: inline-block; margin: 0 " + (gutter / width * 100) + "% " + (gutter / width * 100) + "% 0; width: " + (w / width * 100) + "%;",
		l = rows * cols,
		i, box;
    var randNum =  Math.floor(Math.random() * 100) + 1;
	for (i = 0; i < l; i++) {
		box = document.createElement("div");
		box.style.cssText = css;
    box.setAttribute("class", className);
    box.index = i;
    box.setAttribute("data-index", i);
    if (vars.onCellClick) {
      box.addEventListener("click", vars.onCellClick);
    }
    if (box.index === 0) {
       box.style.backgroundImage = "url('https://ipfs.io/ipfs/bafybeiafev2vsggt4wodzswroeljcmjcc4oieyhjrbsmr23n3m7lrnyovm/" + randNum + ".png')";
    } else {
        box.style.backgroundImage = "url('https://ipfs.io/ipfs/bafybeiafev2vsggt4wodzswroeljcmjcc4oieyhjrbsmr23n3m7lrnyovm/" + box.index +randNum + ".png')";
    } 
		container.appendChild(box);
	}
	container.style.cssText = "width:" + width + "px; line-height: 0; padding:" + gutter + "px 0 0 " + gutter + "px; display:inline-block;";
	parent.appendChild(container);
	return container;
}

//this just helps avoid the pixel-snapping that some browsers do.
gsap.set(".ii-box", {rotation: 0.5, force3D: true});

}

function logo_anima(){    
    var logo = ".ii-logo" 
    la = gsap.timeline({ repeat: 0 });
       la.to(logo, { duration: 0.2, scale: 0 })
         .to(logo, { duration: 1, scale: 1 })   
         .to(logo, { duration: 0.25, rotation: 360,
                    transformOrigin: "center center", 
                    ease: "Power2.easeInOut"
     }) 
    }


function create_arrow(){
  var ia = document.createElement("div");
      ia.setAttribute("class", "ii-ar");
  var arrow_div = document.querySelector("#ii-arrow-div");
      arrow_div.appendChild(ia);
    
  }

function arrow_anima(){
var ar = ".ii-ar",
    ud = gsap.timeline({ repeat: -1 });
ud.to(ar, { y: -30, duration: 1, yoyo: true,  ease: "none" })
  .to(ar, { y: 0, duration: 0.2, yoyo: true,  ease: "none" })
  .to(ar, { y: 30, duration: 0.2, yoyo: true,  ease: "none" })
  .to(ar, { y: 0, duration: 0.5, yoyo: true,  ease: "none" });
  
}

//** SECTION ANIMATIONS */
gsap.to("#ii-anim-container", {
  scrollTrigger: {
    trigger: "#ii-anim-container",
    scrub: 0.6,
    start: "top 85%",
    end: "top 45%",
	markers: false
  },
//   x: 0,
rotation: 360,
  transformOrigin: "center center", 
  ease: "Power2.easeInOut"
});  

var txt = ".txt-sketch";
var txt_plan = ".txt-plan";
var txt_team = ".txt-team";
var sketches = ".ii-drawings";

sec3 = gsap.timeline({ repeat: -1 });
  sec3.to(txt, {
    scrollTrigger: {
      trigger: txt,
      scrub: 0.6,
      start: "center bottom",
    markers: false
    }, 
    x: 800,
    opacity: 1,
    duration: 0.5 
})
    .to(sketches, {
      scrollTrigger: {
        trigger: sketches,
        scrub: 0.6,
        start: "top 50%",
        end: "top 10%",
      markers: false
      },
      opacity: 1,
      duration: 0.5,
      //delay: 
    })
    .to(txt_plan, {
      scrollTrigger: {
        trigger: txt_plan,
        scrub: 0.6,
        start: "center bottom",
      markers: false
      }, 
      x: 1400,
      opacity: 1,
      duration: 0.5 
  })
  .to(txt_team, {
    scrollTrigger: {
      trigger: txt_team,
      scrub: 0.6,
      start: "center bottom",
    markers: false
    }, 
    //x: 1400,
    delay: 1,
    opacity: 1,
    duration: 3 
})


   //** NAV-MENU */
   var ii_nav = gsap.timeline()
   ii_nav.to("#ii", {
    '--color': 'white', 
    '--hover-color': "red",
    duration: 10,
    repeat: -1,
    yoyo: true,
    ease: "none"
  });

var master = gsap.timeline();
master.add(create_arrow())
      .add(arrow_anima(), "+=10")
      .add(logo_anima())
      .add(block_anima())     //, "+=60" with a gap of 2 seconds
      //.add(conclusion(), "-=1") //overlap by 1 second


  