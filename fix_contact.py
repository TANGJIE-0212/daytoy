import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

contact_section_pattern = r'<div class=\"relative w-full\">\s*<!-- Form floated right.*?</form>\s*</div>\s*</div>\s*<!-- Wrapping text -->.*?<div class=\"clear-both\"></div>\s*</div>'

new_contact_section = '''<div class="grid grid-cols-1 lg:grid-cols-[1fr_45%] gap-12 lg:gap-24 items-start w-full">
              <!-- Wrapping text on the left -->
              <div class="pt-2 flex flex-col h-full">
                <div>
                  <h2 class="font-display text-[clamp(3.5rem,6.5vw,7.5rem)] leading-[0.9] text-stone-900 mb-8 tracking-tight">
                    If the tone fits,<br />
                    <span class="italic text-stone-500 font-light pr-4">the conversation</span><br />
                    can start here.
                  </h2>

                  <p class="text-xl sm:text-2xl leading-relaxed text-stone-600 mb-16 max-w-xl">
                    This portfolio is an evolving playground. If you see a product worth discussing, a minimal idea worth elaborating, or a collaboration worth trying, drop me note.
                  </p>
                </div>

                <div class="flex flex-col sm:flex-row gap-12 sm:gap-24 mt-auto mb-12 lg:mb-4">
                  <div>
                    <p class="text-xs uppercase tracking-[0.2em] text-stone-400 mb-4">Mail</p>
                    <a href="mailto:contact@daytoy.online" class="block text-xl font-display text-stone-900 hover:text-stone-500 hover:-translate-y-1 transition-all duration-300">contact@daytoy.online</a>
                  </div>
                  <div>
                    <p class="text-xs uppercase tracking-[0.2em] text-stone-400 mb-4">Network</p>
                    <a href="https://github.com/TANGJIE-0212" target="_blank" rel="noopener" class="block text-xl font-display text-stone-900 hover:text-stone-500 hover:-translate-y-1 transition-all duration-300">GitHub / TANGJIE-0212</a>
                  </div>
                </div>
              </div>

              <!-- Form on the right -->
              <div class="relative animate-float-form lg:mt-6">
                <div class="absolute -inset-2 bg-gradient-to-tr from-stone-300 to-white rounded-3xl blur-lg opacity-40"></div>
                <div class="contact-card p-8 sm:p-10 relative">
                  <form id="contactForm" class="space-y-6">
                    <div>
                      <label class="mb-2 block text-sm font-medium text-stone-700">Name</label>
                      <input type="text" name="name" required placeholder="Your name" class="contact-input w-full rounded-2xl px-5 py-4 text-stone-900" />
                    </div>
                    <div>
                      <label class="mb-2 block text-sm font-medium text-stone-700">Email</label>
                      <input type="email" name="email" required placeholder="you@example.com" class="contact-input w-full rounded-2xl px-5 py-4 text-stone-900" />
                    </div>
                    <div>
                      <label class="mb-2 block text-sm font-medium text-stone-700">Message</label>
                      <textarea name="message" required rows="5" placeholder="What's on your mind?" class="contact-input w-full resize-none rounded-2xl px-5 py-4 text-stone-900"></textarea>
                    </div>
                    <button type="submit" id="submitBtn" class="cta-primary w-full rounded-full py-4 text-lg font-medium tracking-wide disabled:cursor-not-allowed disabled:opacity-50 shadow-xl shadow-stone-900/10">Send message</button>
                    <p id="formStatus" class="hidden text-center text-sm mt-4"></p>
                  </form>
                </div>
              </div>
            </div>'''
            
text = re.sub(contact_section_pattern, new_contact_section, text, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Rewrite contact section with grid layout completed')
