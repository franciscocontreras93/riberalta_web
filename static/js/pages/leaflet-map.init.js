function map_init(t,a,o=!1){var s=L.map(t),t=(L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw",{maxNativeZoom:19,maxZoom:25,attribution:'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a> | Desarrollado por <a href="https://www.linkedin.com/in/geofrancisco/">GeoSIG</a>',id:"mapbox/streets-v11",tileSize:512,zoomOffset:-1}),L.tileLayer("http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}",{maxZoom:20,subdomains:["mt0","mt1","mt2","mt3"],attribution:'Desarrollado por <a href="https://www.linkedin.com/in/geofrancisco/">GeoSIG</a>'})),t={"<span>StreetMaps</span>":L.tileLayer("https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",{attribution:'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a> Desarrollado por <a href="https://www.linkedin.com/in/geofrancisco/">GeoSIG</a>',subdomains:"abcd",maxZoom:20}).addTo(s),"<span>Satelital</span>":t};a=L.geoJson(a,{onEachFeature:function(t,a){var o=L.divIcon({html:`<span class="badge badge-outline-dark">${t.properties.codigo}</span>`,className:"mapLabel"}),e=L.marker(a.getBounds().getCenter(),{icon:o}),o=(s.on("zoomend",function(){20<s.getZoom()?e.addTo(s):e.remove(s)}),L.popup()),t=`<div class="row">
            <div class="col-lg-12">
                <div class="card">
                    <div class="card-header">
                        <h4 class="card-title mb-0">${t.properties.codigo}</h4>
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
                                            <td class="customer_name">${t.properties.titular}</td>
                                            <td class="status"><span class="badge badge-soft-warning text-uppercase">N/D</span></td>
                                            

                                        </tr>
                                        
                                    </tbody>
                                </table>
                                
                            </div>
                            
                            
                        </div>
                    </div><!-- end card -->
                    <div class="card-footer">
                    <a class="btn btn-sm btn-success text-white" role="button" href="/components/maps/${t.properties.codigo}" method='GET'>Inspeccion</a>
                    </div>
                </div>
                <!-- end col -->
            </div>
            <!-- end col -->
        </div>
        `;o.setContent(t),s.on("popupopen",function(t){e.remove()}),s.on("popupclose",function(t){e.addTo(s)}),a.bindPopup(o)},style:function(t){if("null"===String(t.properties.titular))return{color:"#d7191c",fillOpacity:"0",stroke:!0,weight:3}}}).addTo(s);o=o&&L.geoJson(o).addTo(s),s.fitBounds(a.getBounds()),L.control.locate().addTo(s),L.control.layers(t).addTo(s)}