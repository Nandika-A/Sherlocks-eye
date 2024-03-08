import { GLTFLoader } from "https://cdn.jsdelivr.net/npm/three@0.121.1/examples/jsm/loaders/GLTFLoader.js";
import { FBXLoader } from "https://cdn.jsdelivr.net/npm/three@0.121.1/examples/jsm/loaders/FBXLoader.js";
import { OrbitControls } from "https://cdn.jsdelivr.net/npm/three@0.121.1/examples/jsm/controls/OrbitControls.js"; // Updated URL

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(
  25,
  window.innerWidth / window.innerHeight,
  0.1,
  100
);
camera.position.z = 1; //set camera on z axis and move by 5
camera.position.x = 1;
camera.position.y = 3;

const currentPath = window.location.pathname;
console.log(currentPath);

const renderer = new THREE.WebGLRenderer({ alpha: true }); //alpha = true makes background transparent
//renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setSize(200, 200); // to make character at bottom

renderer.domElement.style.position = "fixed";
renderer.domElement.style.bottom = "0px";
renderer.domElement.style.right = "0px";

const sceneBox = document.getElementById("scene-box");
sceneBox.appendChild(renderer.domElement);

let mixer;
let shootAction;
let idleAction;
const loader = new GLTFLoader();

//loading character
loader.load("static/Hoodie Character.glb", function (gltf) {
  //https://poly.pizza/m/gKLBoRsyKe
  scene.add(gltf.scene);
  
  gltf.scene.scale.setScalar(1);
  const characterHeight = 1;
  gltf.scene.position.set(0, 5, 0);
  
  mixer = new THREE.AnimationMixer(gltf.scene);
  idleAction = mixer.clipAction(gltf.animations[4]);
  shootAction = mixer.clipAction(gltf.animations[7]);
  idleAction.play();
  camera.position.set(0, 0, 3);
  camera.lookAt(gltf.scene.position);
  window.addEventListener(
    "dblclick",
    function (event) {
      //get the angle and rotate character
      var vector = new THREE.Vector3();
      vector.set(
        (event.clientX / window.innerWidth) * 2 - 1,
        -(event.clientY / window.innerHeight) * 2 + 1,
        0.5
      );
      vector.unproject(camera);
      var dir = vector.sub(camera.position).normalize();
      var distance = -camera.position.z / dir.z;
      var pos = camera.position.clone().add(dir.multiplyScalar(distance));
      var angle = Math.atan2(
        pos.y - gltf.scene.position.y,
        pos.x - gltf.scene.position.x
      );
      gltf.scene.rotation.y = angle >= 0 ? angle : angle + 2 * Math.PI;

      if (mixer) {
        idleAction.enabled = false;
        shootAction.reset().play();
        shootAction.setLoop(THREE.LoopOnce);
        shootAction.clampWhenFinished = true;
      }
    },
    false
  );
  mixer.addEventListener("finished", function (e) {
    if (e.action === shootAction) {
      shootAction.crossFadeTo(idleAction, 1, true); // idle animation when the shoot animation is finished. 
      //crossfade make animation smoother
      shootAction.stop();
    }
  });
});

const clock = new THREE.Clock();
function animate() {
  requestAnimationFrame(animate);

  const delta = clock.getDelta();
  if (mixer) mixer.update(delta);

  renderer.render(scene, camera);
}
const controls = new OrbitControls(camera, renderer.domElement);

animate();

//lighting
const ambientLight = new THREE.AmbientLight("#404040");
scene.add(ambientLight);

const directionalLight = new THREE.DirectionalLight("#ffffff", 2);
directionalLight.position.set(1, 2, 3);
scene.add(directionalLight);

const pointLight = new THREE.PointLight("#ffffff", 1, 100);
pointLight.position.set(50, 50, 50);
scene.add(pointLight);
console.log("main.js loaded");
