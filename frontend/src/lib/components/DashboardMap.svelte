<script>
  import { Search } from "lucide-svelte";
  import MultiSelectComboBoxGrafana from "./MultiSelectComboBoxGrafana.svelte";
  import Button from "./ui/button/button.svelte";
  import * as Tabs from "$lib/components/ui/tabs";

  let selectedQuestions = [];
  const baseURL = "http://localhost:3000/d-solo/adhqdflvh15ogd/map-dashboard?orgId=1&panelId=1"; // eventually change this to the actual URL inside docker
  $: dashboardURL = baseURL

  function handleClick() {
    if (selectedQuestions.length === 0) {
      dashboardURL = baseURL;
      return;
    }
    const selectedQuestionsArrayString = selectedQuestions.join("&var-questions=");
    const newDashboardURL = baseURL + "&var-questions=" + selectedQuestionsArrayString;

    dashboardURL = newDashboardURL;
  }
</script>

<Tabs.Root value="map" class="w-[400px]">
  <Tabs.List>
    <Tabs.Trigger value="map">Mapa</Tabs.Trigger>
    <Tabs.Trigger value="main">Outros Dashboards</Tabs.Trigger>
  </Tabs.List>

  <Tabs.Content value="map">
    <div class="flex items-center display-grid gap-4"> 
      <MultiSelectComboBoxGrafana  bind:values={selectedQuestions}/>
      <Button on:click={handleClick}>
          <Search class="h-5 w-5"/>
      </Button>
    </div>
    
    <iframe title="map-dashboard" src={dashboardURL} width="85%" height="70%" frameborder="0"/>
  </Tabs.Content>

  <Tabs.Content value="main">
      other dashboards will be here in the future.
  </Tabs.Content>
</Tabs.Root>


