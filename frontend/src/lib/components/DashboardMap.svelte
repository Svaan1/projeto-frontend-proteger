<script>
  import { Search } from "lucide-svelte";
  import MultiSelectComboBoxGrafana from "./MultiSelectComboBoxGrafana.svelte";
  import Button from "./ui/button/button.svelte";
  import * as Tabs from "$lib/components/ui/tabs";

  let selectedQuestions = [];
  const baseURL = "http://127.0.0.1:3000/d-solo/"; // eventually change this to the actual URL inside docker
  $: mapDashboardURL = baseURL + "adhqdflvh15ogd/map-dashboard?orgId=1&panelId=1"

  const questionBaseURL = baseURL + "bab249e9-cc93-4af0-833a-a25fe0ac080d/main-dashboard?orgId=1&from=1559858777443&to=1717711577444&panelId=";

  function handleClick() {
    if (selectedQuestions.length === 0) {
      mapDashboardURL = baseURL + "adhqdflvh15ogd/map-dashboard?orgId=1&panelId=1";
      return;
    }
    const selectedQuestionsArrayString = selectedQuestions.join("&var-questions=");
    const newDashboardURL = baseURL + "adhqdflvh15ogd/map-dashboard?orgId=1&panelId=1" + "&var-questions=" + selectedQuestionsArrayString;

    mapDashboardURL = newDashboardURL;
  }
</script>

<Tabs.Root value="map" class="w-[400px]">
  <Tabs.List>
    <Tabs.Trigger value="map">Mapa</Tabs.Trigger>
    <Tabs.Trigger value="questions">Questões</Tabs.Trigger>
    <Tabs.Trigger value="resident-info">Moradores</Tabs.Trigger>
  </Tabs.List>

  <Tabs.Content value="map">
    <div class="flex items-center display-grid gap-4"> 
      <MultiSelectComboBoxGrafana  bind:values={selectedQuestions}/>
      <Button on:click={handleClick}>
          <Search class="h-5 w-5"/>
      </Button>
    </div>
    
    <iframe title="map-dashboard" src={mapDashboardURL} width="85%" height="70%" frameborder="0"/>
  </Tabs.Content>

  <Tabs.Content value="questions">
    Sensitividade Demográfica
    <div class="grid grid-cols-2 gap-20">
      <iframe title="q1" src={questionBaseURL+"2"} width="450" height="200" frameborder="0"/>
      <iframe title="q2" src={questionBaseURL+"3"} width="450" height="200" frameborder="0"/>
      <iframe title="q3" src={questionBaseURL+"4"} width="450" height="200" frameborder="0"/>
      <iframe title="q4" src={questionBaseURL+"5"} width="450" height="200" frameborder="0"/>
      <iframe title="q5" src={questionBaseURL+"6"} width="450" height="200" frameborder="0"/>
      <iframe title="q6" src={questionBaseURL+"18"} width="450" height="200" frameborder="0"/>      
    </div>
  </Tabs.Content>

  <Tabs.Content value="resident-info">
    Moradores
    <div class="grid grid-cols-2 gap-20">
      <iframe title="sex" src={questionBaseURL+"10"} width="450" height="200" frameborder="0"/>                   <!-- Sexo -->
      <iframe title="age" src={questionBaseURL+"17"} width="450" height="200" frameborder="0"/>                   <!-- Idade -->
      <iframe title="sensorial-impairment" src={questionBaseURL+"13"} width="450" height="200" frameborder="0"/>  <!-- Deficiência Sensorial -->
      <iframe title="mobility-impairment" src={questionBaseURL+"12"} width="450" height="200" frameborder="0"/>   <!-- Restrição de Mobilidade -->
      <iframe title="health-impairment" src={questionBaseURL+"15"} width="450" height="200" frameborder="0"/>     <!-- Agravo de Saúde -->
      <iframe title="mental-impairment" src={questionBaseURL+"14"} width="450" height="200" frameborder="0"/>     <!-- Portador de Transtorno / Deficiência Mental -->    
      <iframe title="education" src={questionBaseURL+"16"} width="450" height="200" frameborder="0"/>             <!-- Educação -->
    </div>
  </Tabs.Content>
</Tabs.Root>


