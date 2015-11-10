/**
 * Created by root on 08.06.15.
 */
SearchApp.controller('SearchCtrl', ['$scope', 'SearchFactory', 'CommonData', function($scope, SearchFactory,CommonData) {
    $scope.Types = SearchTypes;
    $scope.Catalogues = SearchCatalogues;
    $scope.ddtypes = ddtypes;
    document.getElementById('nav-active').innerHTML = "Search"

    $scope.CommonData  = CommonData.get()
    if ($scope.CommonData.hasOwnProperty('index') === true){
        $scope.StellarObject = $scope.CommonData;
        $scope.filters = $scope.CommonData.filters;
        $( "div #slider" ).slider({
            step: 0.1,
            range: true,
            max: max_mag,
            min: min_mag,
            values: [ $scope.filters.MinMag, $scope.filters.MaxMag],
            slide: function( event, ui ) {
                $( "#min_mag" ).val($scope.filters.MinMag);
                $( "#max_mag" ).val($scope.filters.MaxMag)
            }
        });


        /*
            if ($.inArray(this.innerHTML, $scope.filters.SearchCatalogues) != -1 || $.inArray(this.innerHTML, $scope.filters.SearchTypes) != -1) {
                this.classList.add("ok")
            }
        })
        */
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
                    console.log('>>')

                })
            } else {
                console.log('><')
                return alert("Geolocation is not supported by this browser.");
            }
            $scope.filters.visible = true;
        }
        else {
            console.log('<')
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
        $('div.box').fadeIn(300);
        $('#results').fadeOut(300);
        $scope.filters.page = page

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
                name: $scope.filters.Name
            }
        ).$promise.then(function(ob){
                $scope.StellarObject = ob;

                $('#results').fadeIn(300);
                $('div.box').fadeOut(300);
            });

    }

    //Wczytywanie kolejnych stron
    $scope.clickNext = function(){
        if ($scope.StellarObject.next != null) {
            page++;
            $scope.SearchFor(page);
        }
    };
    $scope.clickPrevious = function(){
        if (page != 1) {
            page--;
            $scope.SearchFor(page);
        }
    };
    //Caly tr jako link
    $scope.trUrl = function(id, $index){
        /*
         window.open('#/'.concat(url), '_blank');
         */
        CommonData.set($scope.StellarObject,$index, $scope.filters);
        window.location = '#/'.concat(id);
    }
}]);
