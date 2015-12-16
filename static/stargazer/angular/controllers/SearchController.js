/**
 * Created by root on 08.06.15.
 */
SearchApp.controller('SearchCtrl', ['$scope', '$window','SearchFactory', 'CommonData', function($scope, $window, SearchFactory,CommonData) {
    // True if page waits for another part of list
    $scope.pending = false;
    // Data that will be displayed $scope.results

    //Function that initialize slider
    SliderFunc = function(){
        $( "div #slider" ).slider({
            step: 0.1,
            range: true,
            max: max_mag,
            min: min_mag,
            values: [ $scope.filters.MinMag, $scope.filters.MaxMag],
            slide: function( event, ui ) {
                $( "#min_mag" ).val( ui.values[ 0 ]);
                $( "#max_mag" ).val( ui.values[ 1 ]);
                $scope.filters.MinMag = ui.values[ 0 ];
                $scope.filters.MaxMag = ui.values[ 1 ];
            }
        });
    }

    $scope.Types = SearchTypes;
    $scope.Catalogues = SearchCatalogues;
    $scope.ddtypes = ddtypes;
    document.getElementById('nav-active').innerHTML = "Search";
    document.addEventListener('keypress',function(e){var key = e.which || e.keyCode; if (key==13){ $scope.SearchFor(1)}})

    $scope.CommonData  = CommonData.get()
    if ($scope.CommonData.index !== null) {
        $scope.StellarObject = $scope.CommonData.data;
        $scope.filters = $scope.CommonData.filters;
        $scope.results = $scope.CommonData.results;
        $scope.page = $scope.CommonData.page;
        SliderFunc()
        $('#results').fadeIn(300);
    }
    else {
        $scope.filters = {}
        $scope.filters.visible = false;
        $scope.filters.advanced = false;
        $scope.filters.SearchConstellation = [];
        $scope.filters.SearchTypes = [];
        $scope.filters.SearchCatalogues = [];
        $scope.filters.lat = '';
        $scope.filters.MinMag = min_mag;
        $scope.filters.MaxMag = max_mag;
        $scope.page = 1;
        $scope.filters.ordering = 'magnitudo'
        SliderFunc()

        $scope.results = [];


    }

    // JQueryUI
    $( "#autocomplete" ).autocomplete({
        source: ConstList
    });
    //Przyciski
    $scope.ResetFilters = function(){
        $scope.filters.SearchConstellation.length = 0;
        $scope.filters.MaxMag = max_mag;
        $scope.filters.MinMag = min_mag;
        $scope.filters.SearchTypes.length = 0;
        $scope.filters.SearchCatalogues.length = 0;
        $scope.filters.visible = false;
        $scope.filters.lat ='';

        $( "#min_mag" ).val(min_mag);
        $( "#max_mag" ).val(max_mag);
        $( "#slider" ).slider( "values", [ min_mag, max_mag ] );
        $('*> ul > li').removeClass('ok')
    }

    $scope.VisibleOnly = function(){
        if ($scope.filters.visible == false) {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(function(position) {
                    latitude = position.coords.latitude
                    $scope.filters.lat = position.coords.latitude
                    $scope.filters.visible = true;

                })
            } else {
                return alert("Geolocation is not supported by this browser.");
            }
            $scope.filters.visible = true;
        }
        else {
            $scope.filters.visible = false;
            $scope.filters.lat ='';
        }
    }
    $scope.ChooseConst = function(){
        var $acmp = $( "#autocomplete").val();
        $scope.Constellation = $acmp;
        // Sprawdza czy Została dodana taka konstelacja i czy nie jest pusta
        if ($.inArray($acmp,$scope.filters.SearchConstellation ) == -1 && $acmp != '') {
            // Sprawdza czy istnieje taka konstelacja iterując przez ConstList
            for (var index = 0; index < ConstList.length; index++){
                if (ConstList[index].value == $acmp)
                {
                    $scope.filters.SearchConstellation.push($scope.Constellation);
                    $scope.Constellation = null;
                }
            }
        }
        else
        {
            return null
        };
    };
    $scope.RemoveConst = function() {
        return $scope.filters.SearchConstellation.splice($scope.filters.SearchConstellation.indexOf(this.c),1);
    }
    $scope.ChooseType = function(){
        if ($scope.filters.advanced == true){
            if ($.inArray(this.ot.value, $scope.filters.SearchTypes ) == -1) {
                $scope.filters.SearchTypes.push(this.ot.value);
                $scope.filters.SearchTypes.Visible = true;

            }
            else {
                $scope.filters.SearchTypes.splice($scope.filters.SearchTypes.indexOf(this.ot.value), 1)

            }
        }
        else if ($scope.filters.advanced == false)
        {
            if ($.inArray(this.t.uniname, $scope.filters.SearchTypes ) == -1) {
                $scope.filters.SearchTypes.push(this.t.uniname);

            }
            else {
                $scope.filters.SearchTypes.splice($scope.filters.SearchTypes.indexOf(this.t.uniname), 1)

            }

        }
    }
    $scope.ChooseAdvanced = function() {
        if ($scope.filters.advanced == true) {
            $scope.filters.advanced = false;
            $scope.filters.SearchTypes.length = 0;
        }
        else {
            $scope.filters.advanced = true;
            $scope.filters.SearchTypes.length = 0;
            $scope.filters.SearchTypes.length = 0;
        }
    }
    $scope.RemoveType = function(){
        $scope.filters.SearchTypes.splice($scope.filters.SearchTypes.indexOf(this.t), 1);
    }

    $scope.ChooseCatalogue = function(){
        if ($.inArray(this.cat, $scope.filters.SearchCatalogues ) == -1) {
            $scope.filters.SearchCatalogues.push(this.cat);
        }
        else {
            $scope.filters.SearchCatalogues.splice($scope.filters.SearchCatalogues.indexOf(this.cat), 1)
        }
    }
    $scope.RemoveCatalogue = function(){
        $scope.filters.SearchCatalogues.splice($scope.filters.SearchCatalogues.indexOf(this.cat), 1);
    }
    $scope.TypeList = true;
    $scope.CatList = true;

    // Submit przycisk
    $scope.SearchFor = function(page){
        document.getElementById('annotation-loader').style.display = '';
        document.getElementById('params-annot').style.display = '';
        butt = $('#search-btn > input');
        butt.attr('value', 'Search');
        butt.removeAttr('id', 'SearchAgain');
        $('div.box').fadeIn(300);
        $scope.page = page;
        $scope.results= []

        SearchFactory.get(
            {
                page: page,
                max_mag: $scope.filters.MaxMag,
                min_mag: $scope.filters.MinMag,
                adv: $scope.filters.advanced,
                otype:  $scope.filters.SearchTypes.toString(),
                const: $scope.filters.SearchConstellation.toString(),
                cat: $scope.filters.SearchCatalogues.toString(),
                lat: $scope.filters.lat,
                name: $scope.filters.Name,
                orderby: $scope.filters.ordering
            }
        ).$promise.then(function(ob){
                $scope.StellarObject = ob;
                $scope.results = ob.results;
                CommonData.set($scope.StellarObject,1, $scope.filters, $scope.results, $scope.page);

                $('div.box').fadeOut(300);
            });

    }

    //Wczytywanie kolejnych stron

    //Caly tr jako link
    $scope.trUrl = function(id, $index){
        /*
         window.open('#/'.concat(url), '_blank');
         */
        CommonData.set($scope.StellarObject,$index, $scope.filters, $scope.results,$scope.page);
        document.removeEventListener('scroll', LoadOnScroll, false);
        window.location = '/'.concat('object/',id);
    }


    // IE compability
    var doctop = function(){
        if(document.documentElement && document.documentElement.scrollTop)
        {return document.documentElement.scrollTop}
        if(document.body.scrollTop)
        {return document.body.scrollTop}}
    var dochaight =function(){
        if(document.documentElement && document.documentElement.scrollHeight)
        {return document.documentElement.scrollHeight}
        if(document.body.scrollHeight)
        {return document.body.scrollHeight}
        else return 0;}

    //Function downloads new data on scrolling bottom
    function LoadOnScroll(){
        if ($scope.StellarObject && $scope.StellarObject.next !== null ) {
        // Checks if firs part of Data has been downloaded and next data exists
        if (doctop() >  dochaight() - 2200 && $scope.results.length < $scope.StellarObject.count){


                if (!$scope.pending) {
                    $scope.pending = true;
                    document.getElementById('annotation-loader').style.display = 'inherit';
                    SearchFactory.get(

                        {
                            page: +$scope.page + 1,
                            max_mag: $scope.filters.MaxMag,
                            min_mag: $scope.filters.MinMag,
                            adv: $scope.filters.advanced,
                            otype:  $scope.filters.SearchTypes.toString(),
                            const: $scope.filters.SearchConstellation.toString(),
                            cat: $scope.filters.SearchCatalogues.toString(),
                            lat: $scope.filters.lat,
                            name: $scope.filters.Name,
                            orderby: $scope.filters.ordering
                        }
                    ).$promise.then(function(ob){
                            $scope.page++
                            $scope.pending = false;
                            $scope.StellarObject = ob;
                            // appends results to list
                            for (var i = 0; i < ob.results.length; i++){
                                $scope.results.push(ob.results[i]);
                            }
                            CommonData.set($scope.StellarObject,ob.index, $scope.filters, $scope.results, $scope.page);
                            document.getElementById('annotation-loader').style.display = '';



                        })
                }

            }
        }
    };

    document.addEventListener('scroll', LoadOnScroll, false);
    $scope.orderBy =function(data){
        // If order by is changed no next page will be loaded
        if ($scope.filters.ordering == data) {
            $scope.filters.ordering = ''.concat('-',data)
        }
        else if ($scope.filters.ordering == ''.concat('-',data))
        {
            $scope.filters.ordering = '';
        }
        else if ($scope.filters.ordering == '') {
            $scope.filters.ordering = data;
        }
        else { $scope.filters.ordering = data}
    }
    // NIE działa tak jak powinno
    $scope.$watch('filters', function(newdata,olddata) {
        if (!$scope.StellarObject || olddata == newdata ||$scope.results.length == 0){
            return;
        }
        else {
            $scope.StellarObject.next = null;
            $scope.CommonData.next = null;
            butt = $('#search-btn > input');
            butt.attr('value', 'search Again');
            butt.attr('id', 'SearchAgain');
            document.getElementById('params-annot').style.display = 'block';

        }}, true);
}]);
