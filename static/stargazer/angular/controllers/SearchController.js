/**
 * Created by root on 08.06.15.
 */
SearchApp.controller('SearchCtrl', ['$scope', 'SearchFactory', function($scope, SearchFactory) {

    $scope.min_mag = 1.6;
    $scope.max_mag = 18.1;
    $scope.Types = SearchTypes;
    $scope.Catalogues = SearchCatalogues
    $scope.SearchConstellation = [];
    $scope.SearchTypes = [];
    $scope.SearchCatalogues = [];
    $scope.visible = false;
    $scope.lat = ''
    $scope.ddtypes = ddtypes

    // JQueryUI
    $( "#autocomplete" ).autocomplete({
        source: ConstList
    });
    $( "div #slider" ).slider({
        step: 0.1,
        range: true,
        max: $scope.max_mag,
        min: $scope.min_mag,
        values: [ $scope.min_mag, $scope.max_mag],
        slide: function( event, ui ) {
            $( "#min_mag" ).val( ui.values[ 0 ]);
            $( "#max_mag" ).val( ui.values[ 1 ]);
            $scope.MinMag = ui.values[ 0 ];
            $scope.MaxMag = ui.values[ 1 ];
        }
    });



    //Przyciski
    $scope.ResetFilters = function(){
        $scope.SearchConstellation.length = 0;
        $scope.SearchTypes.length = 0;
        $scope.SearchCatalogues.length = 0;
        $scope.visible = false;
        $scope.lat ='';

        $scope.MaxMag = 18;
        $scope.MinMag = 1.6;
        $( "#min_mag" ).val(1.6);
        $( "#max_mag" ).val(18);
        $( "#slider" ).slider( "values", [ 1.6, 18 ] );
        $('*> ul > li').removeClass('ok')
    }

    $scope.VisibleOnly = function(){
        if ($scope.visible == false) {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(function(position) {
                    $scope.lat = position.coords.latitude
                    $scope.visible = true;
                });
            } else {
                return alert("Geolocation is not supported by this browser.");
            }
            $scope.visible = true
        }
        else {
            $scope.visible = false;
            $scope.lat ='';
        }
    }
    $scope.ChooseConst = function(){
        var $acmp = $( "#autocomplete").val();
        $scope.Constellation = $acmp;
        // Sprawdza czy Została dodana taka konstelacja i czy nie jest pusta
        if ($.inArray($acmp,$scope.SearchConstellation ) == -1 && $acmp != '') {
            // Sprawdza czy istnieje taka konstelacja iterując przez ConstList
            for (var index = 0; index < ConstList.length; index++){
                if (ConstList[index].value == $acmp)
                {
                    $scope.SearchConstellation.push($scope.Constellation);
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
        return $scope.SearchConstellation.splice($scope.SearchConstellation.indexOf(this.c),1);
    }
    $scope.ChooseType = function(){
        if ($.inArray(this.t.uniname, $scope.SearchTypes ) == -1) {
            $scope.SearchTypes.push(this.t.uniname);
            $(event.target).addClass('ok');

        }
        else {
            $scope.SearchTypes.splice($scope.SearchTypes.indexOf(this.t.uniname), 1)
            $(event.target).removeClass('ok');

        }
    }
    $scope.RemoveType = function(){
        $scope.SearchTypes.splice($scope.SearchTypes.indexOf(this.t), 1);
    }

    $scope.ChooseCatalogue = function(event){
        if ($.inArray(this.cat, $scope.SearchCatalogues ) == -1) {
            $scope.SearchCatalogues.push(this.cat);
            $(event.target).addClass('ok');
        }
        else {
            $scope.SearchCatalogues.splice($scope.SearchCatalogues.indexOf(this.cat), 1)
            $(event.target).removeClass('ok');
        }
    }
    $scope.RemoveCatalogue = function(){
        $scope.SearchCatalogues.splice($scope.SearchCatalogues.indexOf(this.cat), 1);
    }
    $scope.TypeList = true;
    $scope.CatList = true;

    // Submit przycisk
    $scope.SearchFor = function(page){
        $('div.box').fadeIn(300);
        $('body > section.container > table').fadeOut(300);
        $('body > section.container > span').fadeOut(300);
        SearchFactory.get(
            {
                page: page,
                max_mag: $scope.MaxMag,
                min_mag: $scope.MinMag,
                otype:  $scope.SearchTypes.toString(),
                const: $scope.SearchConstellation.toString(),
                cat: $scope.SearchCatalogues.toString(),
                lat: $scope.lat,
                name: $scope.Name
            }
        ).$promise.then(function(ob){
                $scope.SearchNgc = ob;

                $('body > ng-view > section').fadeIn(300);
                $('div.box').fadeOut(300);
            });

    }

    //Wczytywanie kolejnych stron
    page = 1;
    $scope.clickNext = function(){
        if ($scope.SearchNgc.next != null) {
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
    $scope.trUrl = function(url){
        window.location = '#/'.concat(url);
    }
}]);
