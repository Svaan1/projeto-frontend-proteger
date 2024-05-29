	
<script lang="ts">
    import Check from "svelte-radix/Check.svelte";
    import CaretSort from "svelte-radix/CaretSort.svelte";
    import { tick } from "svelte";
    import * as Command from "$lib/components/ui/command/index.js";
    import * as Popover from "$lib/components/ui/popover/index.js";
    import { Button } from "$lib/components/ui/button/index.js";
    import { cn } from "$lib/utils.js";
    import { createEventDispatcher } from 'svelte';

    const dispatch = createEventDispatcher();

    export let values;
    let isAllSelected = false;
   
    const questions = [
      {
        value: "ALL",
        label: "Todas as questões"
      },
      {
        value: "question_1",
        label: "Questão 01"
      },
      {
        value: "question_2",
        label: "Questão 02"
      },
      {
        value: "question_3",
        label: "Questão 03"
      },
      {
        value: "question_4",
        label: "Questão 04"
      },
      {
        value: "question_5",
        label: "Questão 05"
      },
      {
        value: "question_6",
        label: "Questão 06"
      },
      {
        value: "question_7",
        label: "Questão 07"
      },
      {
        value: "question_8",
        label: "Questão 08"
      },
      {
        value: "question_9",
        label: "Questão 09"
      },
      {
        value: "question_10",
        label: "Questão 10"
      }
    ]; // lol
   
    let open = false;
    values = [];
   
    $: selectedValues =
    values.map((value) => questions.find((f) => f.value === value)?.label).sort().join(" + ") || "Selecione as questões...";
   
    // We want to refocus the trigger button when the user selects
    // an item from the list so users can continue navigating the
    // rest of the form with the keyboard.
    function closeAndFocusTrigger(triggerId: string) {
      open = false;
      tick().then(() => {
        document.getElementById(triggerId)?.focus();
      });
    }
  </script>
   
  <Popover.Root bind:open let:ids>
    <Popover.Trigger asChild let:builder>
      <Button
        builders={[builder]}
        variant="outline"
        role="combobox"
        aria-expanded={open}
        class="w-auto justify-between"
      >
        {selectedValues}
        <CaretSort class="ml-2 h-4 w-4 shrink-0 opacity-50" />
      </Button>
    </Popover.Trigger>
    <Popover.Content class="w-[200px] p-0">
      <Command.Root>
        <Command.Input placeholder="Selecione as questões" class="h-9" />
        <Command.Empty>Não foram encontrada nenhuma questão.</Command.Empty>
        <Command.Group>
          {#each questions as question}
            <Command.Item
              value={question.value}
              onSelect={(currentValue) => {
                if (currentValue === "ALL") {
                  if (isAllSelected) {
                    values = [];
                  }
                  else {
                    values = questions.map((q) => (q.value) != "ALL" ? q.value : null).filter((v) => v !== null);
                  }
                  isAllSelected = !isAllSelected;
                  dispatch('selectedValuesChange', values);
                }

                // if the value is already selected, remove it
                if (values.indexOf(currentValue) > -1 && currentValue !== "ALL") {
                  values = values.filter((v) => v !== currentValue);
                  isAllSelected = false;
                }
                // else add it
                else if (currentValue !== "ALL") {
                  values = [...values, currentValue];
                  if (values.length === questions.length - 1) {
                    isAllSelected = true;
                  }
                }
                dispatch('selectedValuesChange', values);
              }}
            >
              <Check
                class={cn(
                  "mr-2 h-4 w-4",
                  question.value === "ALL" ? !isAllSelected && "text-transparent" : values.indexOf(question.value) === -1 && "text-transparent"
                )}
              />
              {question.label}
            </Command.Item>
          {/each}
        </Command.Group>
      </Command.Root>
    </Popover.Content>
  </Popover.Root>
  
  