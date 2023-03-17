/*
Template Name: Velzon - Admin & Dashboard Template
Author: Themesbrand
Website: https://Themesbrand.com/
Contact: Themesbrand@gmail.com
File: Leaflet init js
*/

// leaflet-map
// var mymap = L.map('leaflet-map').setView([51.505, -0.09], 13);

// L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
//     maxZoom: 18,
//     attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
//         '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
//         'Imagery © <a href="https://www.mapbox.com/">Mapbox</a> | Desarrollado por <a href="https://www.linkedin.com/in/geofrancisco/">GeoSIG</a>',
//     id: 'mapbox/streets-v11',
//     tileSize: 512,
//     zoomOffset: -1
// }).addTo(mymap);







function map_init(map,lote,construcciones=false){

    var mymap = L.map(map);
// console.log(mymap);

var mapbox = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
    maxNativeZoom:19,
    maxZoom: 25,
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
        '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
        'Imagery © <a href="https://www.mapbox.com/">Mapbox</a> | Desarrollado por <a href="https://www.linkedin.com/in/geofrancisco/">GeoSIG</a>',
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1
});

var googleSat = L.tileLayer('http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',{
    maxZoom: 20,
    subdomains:['mt0','mt1','mt2','mt3'],
    attribution: 'Desarrollado por <a href="https://www.linkedin.com/in/geofrancisco/">GeoSIG</a>'
});

var CartoDB_Positron = L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a> Desarrollado por <a href="https://www.linkedin.com/in/geofrancisco/">GeoSIG</a>',
subdomains: 'abcd',
maxZoom: 20
}).addTo(mymap);


var baseMaps = { 
    '<span>StreetMaps</span>':CartoDB_Positron,
    '<span>Satelital</span>':googleSat 
};

function Popup_terrenos(feature,layer) {

    var divIcon = L.divIcon({
        html : `<span class="badge badge-outline-dark">${feature.properties.codigo}</span>`,
        className: 'mapLabel'
    })
    var marker = L.marker(layer.getBounds().getCenter() , {
        icon : divIcon
    })
    
    mymap.on('zoomend', function(){
        if(mymap.getZoom() > 20){
            // console.log(mymap.getZoom())
            marker.addTo(mymap)
        } else{
                marker.remove(mymap)
            }
        })

        var popup = L.popup()
        var popupContent = `<div class="row">
            <div class="col-lg-12">
                <div class="card">
                    <div class="card-header">
                        <h4 class="card-title mb-0">${feature.properties.codigo}</h4>
                    </div><!-- end card header -->

                    <div class="card-body">
                        <div id="details">
                            
                            <div class="table-responsive table-card mt-3 mb-1">
                                <table class="table align-middle table-nowrap" id="customerTable">
                                    <thead class="table-light">
                                        <tr>
                                            <th  data-sort="customer_name">Titular</th>
                                            <th  data-sort="status">Status</th>
                                            
                                        </tr>
                                    </thead>
                                    <tbody class="list form-check-all">
                                        <tr>
                                            <td class="customer_name">${feature.properties.titular}</td>
                                            <td class="status"><span class="badge badge-soft-warning text-uppercase">N/D</span></td>
                                            

                                        </tr>
                                        
                                    </tbody>
                                </table>
                                
                            </div>
                            
                            
                        </div>
                    </div><!-- end card -->
                    <div class="card-footer">
                    <a class="btn btn-sm btn-success text-white" role="button" href="/components/maps/${feature.properties.codigo}" method='GET'>Inspeccion</a>
                    </div>
                </div>
                <!-- end col -->
            </div>
            <!-- end col -->
        </div>
        `;
        popup.setContent(popupContent)
        mymap.on('popupopen',function(e){
            marker.remove()
            // console.log(e)
        })
        mymap.on('popupclose',function(e){
            marker.addTo(mymap)
            // console.log(e)
        })
        layer.bindPopup(popup)
        // layer.bindTooltip(feature.properties.codigo), {
        //     permanent: true
        // }
    }

function styleLayer(feature){
    switch ( String(feature.properties.titular)) { 
        case 'null':
            return {
                
                    color: '#d7191c',
                    fillOpacity: '0',
                    stroke: true,
                    weight: 3
                    
            }
    }
}
var terrenos = L.geoJson(lote,{
    onEachFeature: Popup_terrenos,
    style: styleLayer
}).addTo(mymap)

if (construcciones) {
    var construcciones = L.geoJson(construcciones).addTo(mymap)

};

mymap.fitBounds(terrenos.getBounds())
var lc = L.control.locate().addTo(mymap);
// lc.start()
// console.log('funcionando')
var controlLayers = L.control.layers(baseMaps).addTo(mymap)

}