import { expect } from 'chai'
import { shallowMount } from '@vue/test-utils'
import Theatricals from "../../src/views/Theatricals";

describe('Theatricals.vue', () => {
  it('renders renders button tag', () => {
    const wrapper = shallowMount(Theatricals);
    expect(wrapper.find('button').text()).equal('Знайти')
  })
});

