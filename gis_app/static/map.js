const copy = "© <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors";
const url = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
const osm = L.tileLayer(url, { attribution: copy });
const map = L.map("map", { layers: [osm], minZoom: 5 });
map.
    locate()
    .on("locationfound", (e) => map.setView(e.latlng, 8))
    .on("locationerror", () => map.setView([52.42, 17.00], 10));

async function load_clinics() {
    const clinic_url = `/api/clinics/?in_bbox=${map.getBounds().toBBoxString()}`
    const response = await fetch(clinic_url)
    const geojson = await response.json()
    console.log(geojson)
    return geojson
}
console.log(copy)
console.log(osm)
console.log(map)

async function render_clinics() {
    const clinics = await load_clinics();
    L.geoJSON(clinics)
    .bindPopup((layer) => layer.feature.properties.name)
    .addTo(map);
}

map.on("moveend", render_clinics);

