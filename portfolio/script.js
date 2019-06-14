require([
      "esri/Map",
      "esri/views/MapView",
      "esri/layers/FeatureLayer",
      "esri/widgets/Legend",
      "esri/widgets/Search",
      "esri/widgets/ScaleBar",
      "esri/widgets/Expand",
      "esri/widgets/BasemapGallery",
      "dojo/domReady!"
    ], function(Map, MapView, FeatureLayer, Legend, Search, 
                 ScaleBar, Expand, BasemapGallery) {

      var map = new Map({
        basemap: "topo"
      });

      var view = new MapView({
        container: "viewDiv",
        map: map,
        zoom: 7,
        center: [-119.950, 46.702]
      });
      
      
         
         var firePointsTemplate = {
          title: "Fire Reported!",
          content: "<p><b> Date: {START_DATE} </b></p>" +
            "<p> Cause: {CAUSE}</p>" +
            "<p> Status: {STATUS}</p>" + 
            "<p> Comments: {COMMENTS}</p>" }
         
         var firePoliesTemplate = {
          title: "Fire Reported!",
          content: "<p><b> Date: {START_DATE} </b></p>" +
            "<p> Cause: {CAUSE}</p>" +
            "<p> Status: {STATUS}</p>" + 
            "<p> Comments: {COMMENTS}</p>" }
        
        var firePointsLayer = new FeatureLayer({
          url: "https://services3.arcgis.com/T4QMspbfLg3qTGWY/arcgis/rest/services/NWCC_Operational_Layers/FeatureServer/0/updateFeatures",
                
          outFields: ["*"],
          popupTemplate: firePointsTemplate
        });
  
        var firePoliesLayer = new FeatureLayer({
          url: "https://services3.arcgis.com/T4QMspbfLg3qTGWY/arcgis/rest/services/NWCC_Operational_Layers/FeatureServer/4/updateFeatures",
                
          outFields: ["*"],
          popupTemplate: firePointsTemplate
        });
  
  
        var legend = new Legend({
          view: view
        });
  
        var search = new Search({view:view})
        
        var scaleBar = new ScaleBar({
          view: view
        })
        
        var bm = new BasemapGallery({view:view, container: document.createElement("div")})
        
        var bgExpand = new Expand({
          view: view,
          content: bm,
          collapseIconClass: "esri-icon-minimize"
        })

        bm.watch("activeBasemap", function() {
          var mobileSize =
            view.heightBreakpoint === "xsmall" ||
            view.widthBreakpoint === "xsmall";

          if (mobileSize) {
            bgExpand.collapse();
          }
        })
        
        view.ui.add(scaleBar, {
          position: "bottom-right"
        })
        
        view.ui.add(search, {
          position: "bottom-left",
          index: 2
        })
  
        view.ui.add(legend, "top-left");
  
        view.ui.add(bgExpand, {position:"bottom-left"})

        //map.add(featureLayer);
        map.add(firePointsLayer);
        map.add(firePoliesLayer);
  
});